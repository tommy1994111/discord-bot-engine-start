import discord
from bot import EngineStartBot

def check_message_has_string(*target_strings: str):
    def one_of_targets_in_content(content: str):
        return True in [target in content for target in target_strings]

    def decorator(func):
        async def wrapper(message: discord.Message):
            if (one_of_targets_in_content(message.content)):
                await func(message)
        return wrapper
    return decorator

def register_listeners(bot: EngineStartBot):
    @bot.listen('on_message')
    @check_message_has_string('你媽')
    async def your_mom(message: discord.Message):
        # 阿威
        await message.add_reaction('<:a0a17:686544937147170838>')


    @bot.listen('on_message')
    @check_message_has_string('空幹')
    async def kon_gan(message: discord.Message):
        await message.add_reaction('<:overloadKon:819226031352184863>')
        await message.add_reaction('<:overloadGan:819226031101444146>')


    @bot.listen('on_message')
    @check_message_has_string('哭啊', '哭阿')
    async def kon_gan(message: discord.Message):
        await message.add_reaction('<:relaxingCry:832972506335019008>')


    @bot.listen('on_message')
    @check_message_has_string('屁眼')
    async def pee_yan(message: discord.Message):
        await message.add_reaction('<:nlnlOUO:666894208514392064>')
