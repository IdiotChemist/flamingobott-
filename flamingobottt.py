import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time
import youtube_dl

Client = discord.Client()
client = commands.Bot(command_prefix ="f?")
client.remove_command('help')


players = {}
queues = {}
def check_queues(id):
    player = queues[id].pop(0)
    players[id]= player
    player.start()

@client.event
async def on_ready():
    print("Flamingobot is ready")

def __init__(self, bot):
        self.bot = bot
@client.command()
async def hi():
    await client.say('hi')
@client.command(pass_context=True)
async def play(ctx, url):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)  
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))
    players[server.id] = player
    player.start()
    
@client.command()
async def thonk():
    await client.say(':thinking:')
@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ' '
    await client.say(output)
@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()
@client.command(pass_context=True)
async def clear(ctx, amount=20):
    await client.say('**woops! you can only delete messages that are under 14 days old**')
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Messages deleted uwu')

@client.command(pass_context=True)
async def pause(ctx):
    id = ctx.message.server.id
    players[id].pause()
@client.command(pass_context=True)
async def resume(ctx):
    id = ctx.message.server.id
    players[id].resume()
@client.command(pass_context=True)
async def stop(ctx):
    id = ctx.message.server.id
    players[id].stop()

@client.command(pass_context=True)
async def queue(ctx, url):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    player = await voice_client.create_ytdl_player(url, after=lambda: check_queue(server.id))

    if server.id in queues:
        queues[server.id].append(player)
    else:
        queues[server.id] = [player]
    await client.say('Video queued')

    



@client.command()
async def displayembed():
    embed = discord.Embed(
        title = 'title',
        description = 'This is a desc',
        color = discord.Color.blue()
        )

    embed.set_footer(text='Hello!.')
    embed.set_image(url='https://s.aolcdn.com/hss/storage/midas/5b90065e72b963836a64837dee9ce7d0/204504948/IMG_0017.jpg')
    embed.set_thumbnail(url='https://static.businessinsider.com/image/5b7050cd8ea82f94598b4da6-750.jpg')
    embed.set_author(name ='Author name',
    icon_url='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_bEU2rkaqg7fywL1zDf-YB-9No5vuTUhNEMHavW5wh3FQTLi6')
    embed.add_field(name='Field Name', value='Field Value', inline=False)
    embed.add_field(name='Field Name', value='Field Value', inline=True)
    embed.add_field(name='Field Name', value='Field Value', inline=True)

    await client.say(embed=embed)



@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        color = discord.Color.orange()
    )

    embed.set_author(name='help')
    embed.add_field(name='f?hi', value='Say hi to me!', inline=False)
    embed.add_field(name='f?thonk', value='**B I G  T H O N K**', inline=False)
    embed.add_field(name='f?join', value='Joins the voice channel', inline=False)
    embed.add_field(name='f?leave', value='Leaves the voice channel', inline=False)
    embed.add_field(name='f?clear', value='Clears all the messages from under 14 days (**mods/admins only!!**) ', inline=False)
    embed.add_field(name='f?echo', value='Echos your message', inline=False)
    embed.add_field(name='f?play', value='Plays you some tunes', inline=False)
    embed.add_field(name='f?pause', value='Stops the tunes', inline=False)
    embed.add_field(name='f?resume', value='Resumes your groovy jams', inline=False)
    embed.add_field(name='f?stop', value='End your groovy session', inline=False)
    embed.add_field(name='f?queue', value='Queue your song (note that you have to use f?queue in order for the song to play if theres already a song playing)', inline=False)


    await client.send_message(author, embed=embed)
    

    



client.run("NDg4ODg3MDg4OTM5MjcwMTY1.DoGGpQ.mUNslZ0jpnb6Bi3uDTsu3ZNIA90")




            
