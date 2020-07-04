import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Black Lives Matter"))
    print('Bot is ready to rumble')


# Command to load extensions from cogs folder (for example commands etc)
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    

# Command to unload extensions from cogs folder
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    

# Command to reload extensions (used for live adding/updating of commands)
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


# User command temporarily saved here until problem with cog is solved
@client.command(aliases=['u'])
async def users(ctx):
    id = client.get_guild(563446469844271104)
    await ctx.send(f'The server has {id.member_count} members!')

# Iterating through cogs folder to import all extension files
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


# Set proper token and run the bot
client.run('NzI4NTMwNjU1ODQ3MTIwOTY3.Xv7vmg.la8FrikKw50EpJgfyjcikwAsTmg')