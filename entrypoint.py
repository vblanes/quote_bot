from telegram_api_utils import get_bot_updates, get_last_update_id
import time

def process_update(update: dict) -> None:
    """
    Analyze and perform actions depending on the content of each update
    This is the logic core of the aplication!
    """
    pass

def main_loop(bot_url) -> None:
    last_update_id = None
    while True:
        updates = get_bot_updates(url=bot_url, offset=last_update_id)
        # sanity check
        if 'result' in updates and len(updates.get('result')) > 0:
            last_update_id = get_last_update_id(updates=updates)
            # Calls the logic core of the bot secuentally
            # This can be paralelized
            for update in updates:
                process_update(update)
            # be gentle with telegram servers
            # TODO this could be parametrized
            time.sleep(1)

if __name__ == '__main__':
    main_loop()