import os
import logging
import json
from dotenv import load_dotenv
import discord
from discord.ext import commands

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

# read commands
COMMANDS = None
with open('command.json') as file:
    COMMANDS = json.load(file)


class EngineStartContext(commands.Context):
    async def tick(self, value):
        emoji = '\N{WHITE HEAVY CHECK MARK}' if value else '\N{CROSS MARK}'
        try:
            await self.message.add_reaction(emoji)
        except discord.HTTPException:
            # sometimes errors occur during this, for example
            # maybe you don't have permission to do that
            # we don't mind, so we can just ignore them
            pass


class EngineStartBot(commands.Bot):
    async def get_context(self, message, *, cls=EngineStartContext):
        return await super().get_context(message, cls=cls)


bot = EngineStartBot(command_prefix='$')

# commands
@bot.command('debug')
async def debug(ctx: EngineStartContext, *inputs):
    print('MESSAGE: ', inputs)

@bot.command()
async def guess(ctx: EngineStartContext, number: int):
    value = 7414
    await ctx.tick(number == value)

@bot.command('引擎發動')
async def engine_start(ctx: EngineStartContext):
    await ctx.message.reply(content=f"```{COMMANDS['engine_start']}```")

@bot.command('OSN')
async def osn(ctx: EngineStartContext):
    await ctx.message.reply(content=f"```{COMMANDS['osn']}```")

@bot.command('FOFO')
async def fofo(ctx: EngineStartContext):
    await ctx.message.reply(content=f"```{COMMANDS['fofo']}```")

@bot.command('90在幹嘛')
async def whats_90_doing(ctx: EngineStartContext):
    await ctx.message.reply(content=COMMANDS['whats_90_doing'])

def check_message_has_string(target_string: str):
    def decorator(func):
        def wrapper(message: discord.Message):
            if target_string in message.content:
                func()
        return wrapper
    return decorator

# listen messages
@bot.listen('on_message')
async def your_mom(message: discord.Message):
    if ('你媽' in message.content):
        # 阿威
        await message.add_reaction('<:a0a17:686544937147170838>')

@bot.listen('on_message')
async def kon_gan(message: discord.Message):
    if ('空幹' in message.content):
        await message.add_reaction('<:overloadKon:819226031352184863>')
        await message.add_reaction('<:overloadGan:819226031101444146>')


@bot.listen('on_message')
async def kon_gan(message: discord.Message):
    if ('哭啊' in message.content):
        await message.add_reaction('<:relaxingCry:832972506335019008>')

bot.run(token)