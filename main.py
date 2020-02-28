import os

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

# vc = None

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    
    # see all emojis
    # for guild in client.guilds:
    #     print(guild.emojis)



@client.event
async def on_message(message):
    # vc = client.get_channel(525304043082612745)
    if message.author == client.user:
        return

    if message.content == '!引擎發動':
        await message.channel.send('''```轟隆隆隆🤣🤣隆隆隆隆衝衝衝衝😏😏😏拉風😎😎😎引擎發動🔑🔑🔑引擎發動+🚗+👉+🚗
風 💨💨 吹動每一個毛孔👩🦲🧔 我是今夜🌙🌙 最😎 稀有的品種🤓🤓 讓😯 看到的人以為是夢😱😱 還沒醒來😴😴 就已經無影無蹤👻👻 風 💨💨 敲醒每一個面孔😲😲 我是明天🤙🤙 被 贊嘆的驚悚😵😵 讓😨😨 看到的人全部感動😭😭 0⃣到💯K only 4⃣秒鐘😏😏
紅燈停 綠燈行🚥🚥 看到行人要當心🚶♀🚶♀ 快車道 慢車道😈😈 平安回家才是王道 💪💪 開車🚗🚗不是騎車🏍🏍不怕沒戴安全帽👲👲只怕警察👮♂👮♂BI BI BI 叫我路邊靠 😩😩 BI BI BI BI BI 大燈忘了開😏😏 BI BI BI BI BI 駕照沒有帶 🤫🤫 BI BI BI BI BI 偷偷講電話😎😎 BI BI BI BI BI 沒繫安全帶 😬😬 我的夢幻車子🚗🚗就是最辣🌶🌶的美女👸👸 有她陪伴😏😏哪怕車上只有收音機 📻📻 我就像隻野狼🐺🐺身上披著羊🐑🐑的皮 我的心情🤪🤪好比開著一架戰鬥機🛩🛩```''')

    if (message.content == '!OSN'):
        await message.channel.send('''```I ’m still the same😎🤙🤙都好像沒有變🙄🙄Nothing changed👏👏還是討厭下雨天🌧🌧還是不愛認錯😨😨脾氣是硬了點😱😱 這我都清楚但我沒有辦法改變😗😜我後悔高中花錢裝很吵的排氣管😔😔 想努力賺錢養妳 卻養成了壞習慣😒😤 我還想帶妳到處晃晃到處帶妳玩🥰😘 Cuz me without you it feels like😎```''')

    if (message.content == '!FOFO'):
        await message.channel.send('''```我也是醉了他媽的🙄🙄剛剛團練 媽的 輔野差距👊👊👊然後 說 我中路康特💪🏼💪🏼然後對面一直靠😡😡然後 我沒辦法把他打爆😤😤然後他媽打完 然後 我說 然後 因為這些視野 他們靠的問題😒😒然後打野就說 我感覺你也沒辦法把他打爆😞 幹你娘機掰🖕 真的很不爽 無言💤```''')


    if (message.content == '!90在幹嘛'):
        await message.channel.send('''在睡覺 <:ResidentSleeper:569834842536280075>''')
    # if message.content == '!召喚阿亮':
    #     # print('召喚阿亮', vc)
    #     # vc = client.get_channel(525304043082612745)
    #     await vc.connect()
    #     await message.channel.send('!play 超跑情人夢')

    # if message.content == '!88':
    #     print(client.voice_channels)
    #     # await client.voice_channels

client.run(token)