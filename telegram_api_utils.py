import json
import request
from urllib.parse import quote_plus
from typing import Tuple

"""
Class with function to interact with the Telegram APIS
"""

def request_url_content(url: str) -> dict:
    response = requests.get(url)
    content = response.content.decode("utf8")
    return json.loads(content)

def get_bot_updates(url: str, offset: int = None) -> dict:
    #TODO check if we really use the offset part
    url = url + "getUpdates"
    if offset:
        url += f"?offset={offset}"       
    js = request_url_content(url)
    return js

def get_last_update_id(updates: list) -> int:
    return max([int(el['update_id']) for el in updates['result']])


def send_message(message: str, telegram_id: int, reply_markup=None) -> dict:
    text = quote_plus(text)
    url = URL + f"sendMessage?text={message}&chat_id={telegram_id}&parse_mode=Markdown"
    # reply_markup is for a special keyboard
    # TODO we need keyboards??
    if reply_markup:
        url += f"&reply_markup={reply_markup}"
    return request_url_content(url)

    """
    May we need other multimedia stuff such as send files, images, forward messages...
    """

def extract_update_info(update: dict) -> Tuple[int, int, str]:
    """
    Obtain the telegram from the sender
    """
    if 'message' in update and 'text' in update.get('message'):
        telegram_id: int = update.get('message').get('chat', {}).get('id')
        message_id: int = update.get('message').get('message_id')
        content: str = update.get('message').get('text').strip()

    elif 'callback_query' in update:
        telegram_id: int = update.get('callback_query').get('from', {}).get('id')
        message_id: int = update.get('callback_query').get('message', {}).get('message_id')
        content: str = update.get('callback_query').get('data')

    else:
        return None, None, None
       
    return telegram_id, message_id, content
