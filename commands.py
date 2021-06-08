import json
from discord.ext import commands
from bot import EngineStartContext

# read commands
COMMANDS = None
with open('command.json') as file:
    COMMANDS = json.load(file)

def register_commands(bot: commands.Bot):
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
