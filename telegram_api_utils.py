import json
import request
from urllib.parse import quote_plus

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

def telegram_id(update: dict) -> int:
    """
    Obtain the telegram from the sender
    """
    if 'edited_message' in update and 'text' in update.get('edited_message'):
        return update.get('edited_message').get('chat').get('id')

    elif 'callback_query' in update:
        return update.get('callback_query').get('from').get('id')

    else:
        return update.get('message'.get('chat').get('id')
