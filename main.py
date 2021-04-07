import discord
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot(command_prefix='', intents=intents)

@Bot.event
async def on_ready():
    print("Ah shit! Here we go again...")
    await Bot.change_presence(activity = discord.Activity(type = discord.ActivityType.listening, name= "Mavi Ziller Konağı"))

@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name="🖐│hoş-geldiniz")
    await channel.send(f"Aramıza bir Expired daha katıldı. Hoş geldin {member.mention} !")
    print(f"Aramıza bir Expired daha katıldı. Hoş geldin f{member.mention} !")
    role = discord.utils.get(member.guild.roles, name="Expireds")
    await member.add_roles(role)


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name="🎉│bestsellers")
    await channel.send(f"{member.mention} en çok satanlarda şimdi bir numara!")
    print(f"{member.mention} en çok satanlarda şimdi bir numara!")


@Bot.command()
async def major(msg):
    await msg.send('Ya müzik yapıyordur ya da dertzzz çalışıyordur.')

@Bot.command()
async def seyidcem(msg):
    await msg.send('Ya müzik yapıyordur ya da dertzzz çalışıyordur.')

@Bot.command()
async def hr(msg):
    await msg.send('Hrrrrr...')

@Bot.command()
async def miyav(msg):
    await msg.send('Miyav miyav miyaaav! :cat:')

@Bot.command()
async def mert(msg):
    await msg.send('Gitar çalıyordur muhtemelen. :guitar:')

@Bot.command()
async def ogi(msg):
    await msg.send('Seni yapıyor.')

@Bot.command()
async def oğuz(msg):
    await msg.send('Seni yapıyor.')

@Bot.command()
async def furkan(msg):
    await msg.send('Kesin Türk Sanat Müziği yapıyordur. :violin:')

@Bot.command()
async def ahmet(msg):
    await msg.send('Solo atıyor. :love_you_gesture:')

@Bot.command()
async def oktay(msg):
    await msg.send('Büyük ihtimalle toksiklik yapıyordur. :radioactive:')

@Bot.command()
async def seymen(msg):
    await msg.send('Earrape yapıyordur. :ear:')

@Bot.command()
async def minör(msg):
    await msg.send('Miyav. :smiley_cat:')

@Bot.command()
async def minor(msg):
    await msg.send('Miyav. :smiley_cat:')

@Bot.command()
async def kaan(msg):
    await msg.send('Dışarıda geziyordur. :mask:')

@Bot.command()
async def ev_yapalım(msg):
    await msg.send('Olmaz.')

@Bot.command()
async def hamza(msg):
    await msg.send("Oktay'a toksiklik yapmasında yardımcı oluyor.")

@Bot.command()
async def irem(msg):
    await msg.send("Sövüş Discord'unda gezip, şarkı söylüyor.")

@Bot.command()
async def yaren(msg):
    await msg.send('Kayısı toplayıp, dertzzz yapıyor.')

@Bot.command()
async def kaptan(msg):
    await msg.send('Gemi sürüyor. Tamam komik değildi.')

@Bot.command()
async def şey_mi_dostum(msg):
    await msg.send('Yine yangınlaağağağar yine beeeğn')

@Bot.command()
async def sa(msg):
    await msg.send('Ass.')

@Bot.command()
async def amk(msg):
    await msg.send('Aaa terbiyeliğiği')

@Bot.command()
async def mzk(msg):
    await msg.send("https://open.spotify.com/artist/7t0LeW7MAw5JFrZGq4sj1x?si=4mr9Z5o6SN2lhqd13vfltQ linkinden Majör'ümüzün elinden çıkmış şarkılara ulaşabilirsin.")

@Bot.command()
async def twitch(msg):
    await msg.send("https://twitch.tv/majorexpired 'da yayınlara bekleriz efenim.")

@Bot.command()
async def twitch_duyuru(msg):
    await msg.send("https://twitch.tv/majorexpired Bütün dünya (!) izler durur. Peki ya sen; var mısın? Yooooksun! @everyone")

@Bot.command()
async def gb(msg):
    await msg.send('Biz bir aileyiz.')


Bot.run('ODI0MjU3OTE1MjkyNjE0NjY3.YFswAA.jqwR2fuY9fZIHUOnlgtxhE45rp0')