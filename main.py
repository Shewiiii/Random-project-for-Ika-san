import discord
import os
from dotenv import load_dotenv
import logging

from modules.youtube_ import get_vid_id
from modules.daily import get_daily

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
)

load_dotenv()
TOKEN = os.getenv('GEKIYABAHIMITSUTOKEN')
bot = discord.Bot()


@bot.command(name="ping")
async def ping(ctx: discord.ApplicationContext) -> None:
    latency = round(bot.latency*1000, 2)
    logging.info(f'Pinged latency: {latency}')
    await ctx.respond(f'あわあわあわわわ ! {latency}ms')


@bot.command(
    name="asmr",
    description="Get a random asmr video from Ika's playlist x)"
)
async def asmr(ctx: discord.ApplicationContext) -> None:
    dico = get_vid_id()
    if not dico:
        await ctx.respond('No ASMR <:8_:1005710232246300772>')
    video_id = dico['video_id']
    playlist_id = dico['playlist_id']
    await ctx.respond(
        f'https://www.youtube.com/watch?v={video_id}'
        f'&list={playlist_id}'
    )


@bot.command(
    name="daily",
    description="Daily ASMR"
)
async def daily(ctx: discord.ApplicationContext) -> None:
    dico = get_daily()
    if not dico:
        await ctx.respond('No ASMR for today <:8_:1005710232246300772>')
    await ctx.respond(
        "Today's ASMR: "
        f'https://www.youtube.com/watch?v={dico['video_id']}'
        f'&list={dico['playlist_id']}'
    )

bot.run(TOKEN)
