from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
from dotenv import load_dotenv
from random import randint

load_dotenv()
API_KEY = os.getenv('GOOGLEAPIKEY')
youtube = build('youtube', 'v3', developerKey=API_KEY)


def get_vid_id(
    playlist_id: str = 'PL3IFHunJwdt_5ux6D3T7UJqJvRIRFGjgP'
) -> dict | None:
    '''Get the id of a vid in a given playlist
    '''
    # items, a list with video infos, like:
    # {'kind': 'youtube#playlistItem',
    #  'etag': '36YzvA8ArGmwP7CCW_6w8lngB3w',
    #  'id': 'UEwzSUZIdW5Kd2R0XzV1eDZEM1Q3VUpxSnZSSVJGR2pnUC4yODlGNEE0NkRGMEEzMEQy',
    #  'contentDetails': {'videoId': 'SvUvSRe-9YE',
    #   'videoPublishedAt': '2023-11-01T19:04:02Z'}
    # },
    # ...
    items = []
    next_page_token = None

    while True:
        request = youtube.playlistItems().list(
            part='contentDetails',
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        )
        try:
            response = request.execute()
        except HttpError:
            return
        next_page_token = response.get('nextPageToken')

        items += response['items']

        if not next_page_token:
            break

    items_count = len(items)
    # If playlist empty
    if items_count == 0:
        return
    available = False
    tries = 0

    while (not available
           and tries <= items_count):
        index = randint(0, items_count-1)
        selected_id = items[index]['contentDetails']['videoId']
        if 'videoPublishedAt' in items[index]['contentDetails']:
            available = True
        tries += 1

    if selected_id:
        dico = {
            'video_id': selected_id,
            'playlist_id': playlist_id
        }
        return dico


if __name__ == '__main__':
    print(get_vid_id())
