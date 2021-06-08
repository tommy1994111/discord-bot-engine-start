import discord
from discord.ext import commands

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

