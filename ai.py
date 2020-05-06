import discord
import os
client = discord.Client()

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("~명령어를 쳐서 명령어를 확인하세요")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content.startswith("~명령어"):
        await message.channel.send("명령어:~채널, ~크루, ~트위치, ~정보, ~핑")
    if message.content.startswith("~채널"):
        await message.channel.send("쉰김치 유튜브 채널입니다 https://www.youtube.com/channel/UC9GATWJ_c2njfsORBn6bk1Q?view_as=subscriber")
    if message.content.startswith("~크루"):
        await message.channel.send("시리우스")
    if message.content.startswith("~트위치"):
        await message.channel.send("쉰김치 트위치입니다 https://www.twitch.tv/kimchishin")
    if message.content.startswith("~정보"):
        await  message.channel.send("심심해서 쉰김치가 만든 봇입니다")
    if message.content.startswith("~핑"):
        await  message.channel.send("{}ms".format(int(1000 * client.latency)))


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
