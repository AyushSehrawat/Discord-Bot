# Enable Developer Mod in discord , go to appearances and on developer mod :)
import discord

import discord_pass

from discord.ext import commands, tasks

from itertools import cycle

import os

import random

import jokeapi

client = commands.Bot(command_prefix='--', intents = discord.Intents.all())

client.remove_command("help")

status = cycle(
    ['Try --help', 'Try --server', 'Try --help', 'Try --8ball', 'Try --password', 'Try --spam'])

unicode_list = ["\U0001f600", "\U0001f970",
                "\U0001f609", "\U0001f60a", "\U0001f971"]

@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready')

    channel = client.get_channel(id=756735145997762634)    # Your any channel id

    await channel.send(f'Hi! I am `online!`')


@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


@client.event
async def on_member_join(member : discord.Member):

    first_role = member.guild.get_role(757518078270636113)  # So, i have a role Developers, whose id is this.

    await member.add_roles(first_role)

@client.command(aliases=['hi'])
async def hello(ctx):
    msg = await ctx.send(f'Hello {ctx.author.mention}')

    msg

    await msg.add_reaction(f'{random.choice(unicode_list)}')

@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extensions):
    client.load_extension(f'cogs.{extensions}')


@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extensions):
    client.unload_extension(f'cogs.{extensions}')

# Enable / Disable Command

@client.command()
@commands.has_permissions(administrator=True)
async def d_spam(ctx):
    c = client.get_command("spam")
    c.enabled = False
    await ctx.send('Spam Command is disabled')

@client.command()
@commands.has_permissions(administrator=True)
async def e_spam(ctx):
    d = client.get_command("spam")
    d.enabled = True
    await ctx.send('Spam Command is enabled')

@client.command()
@commands.has_permissions(administrator=True)
async def d_pass(ctx):
    d = client.get_command("password")
    d.enabled = False
    await ctx.send('Password Command is disabled')

@client.command()
@commands.has_permissions(administrator=True)
async def e_pass(ctx):
    d = client.get_command("password")
    d.enabled = True
    await ctx.send('Password Command is enabled')

# Password command . Due to some issues, it's in main file


@client.command()
async def password(ctx, passlength=10):
    passlength = int(passlength)
    if passlength > 51:
        await ctx.send(f'{ctx.author.mention} Your password cannot be so long!')
    elif passlength < 51:
        passwor = discord_pass.secure_password_gen(passlength)
        await ctx.send(f'{ctx.author.mention} Check your dm for the password! ')
        await ctx.author.send(f'You password is \n `{passwor}`')

# Joke command here, since it's reading all file in cogs as cogs, but joke-api file isn't a cog. 
@client.command()
async def joke(ctx):
    jokes = jokeapi.get_joke()
    if not jokes:
        await ctx.channel.send("Couldn't get joke from API. Try again later.")

    else:
        await ctx.channel.send(jokes['setup'] + '\n' + jokes['punchline'])



# Slang Filter Here ! Sorry for nay abuse :()

filtered_words = ['fuck','bitch']

@client.event
async def on_message(msg):
    for word in filtered_words:
        if word in msg.content.lower():
            await msg.delete()

    await client.process_commands(msg)

# Slang filter ends

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


client.run('Token')  #Here goes your token in ''
