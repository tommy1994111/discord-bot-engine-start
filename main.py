import os
import logging
from dotenv import load_dotenv
from bot import EngineStartBot
from commands import register_commands
from listeners import register_listeners

# get environment variables
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

# logging section
logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger('discord')
# logger.setLevel(logging.DEBUG)
# handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
# handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
# logger.addHandler(handler)


if (__name__ == '__main__'):
    bot = EngineStartBot(command_prefix='$')
    register_commands(bot)
    register_listeners(bot)
    bot.run(token)
