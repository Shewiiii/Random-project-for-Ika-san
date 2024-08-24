
import json
from datetime import datetime
from modules.youtube_ import get_vid_id


def new_daily(
    playlist_id: str,
    filename: str = 'idk'
) -> dict | None:
    dico = get_vid_id(playlist_id)
    if not dico:
        return
    data = {
        "date": datetime.now().strftime("%Y-%m-%d"),
        "dico": dico
    }
    with open(f'{filename}.json', 'w') as file:
        json.dump(data, file, indent=4)

    return dico


def get_daily(
    playlist_id: str,
    filename: str = 'idk'
) -> dict | None:
    with open(f'{filename}.json', 'r') as file:
        data = json.load(file)

    saved_date = data['date']
    today = datetime.now().strftime("%Y-%m-%d")
    if saved_date != today:
        data['dico'] = new_daily(playlist_id)

    return data['dico']
