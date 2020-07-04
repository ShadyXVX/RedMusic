import discord
from discord.ext import commands
import logging
import random

commandsList = """**Commands List:**

To greet the bot type: -hello
To get a list of all commands type: -Help
To get the number of users on this server type: -users
To clear x messages type: -clear x"""


client = commands.Bot(command_prefix='-')
id = client.get_guild(563446469844271104)


class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['h'])
    async def Help(self, ctx):
        await ctx.send(commandsList)

    # @commands.command(aliases=['u'])
    # async def users(self, ctx):
    #     await ctx.send(f'The server has {id.member_count} members!')

    @commands.command(aliases=['hi'])
    async def hello(self, ctx):
        await ctx.send('Hi, I am RedMusic! --- type -Help for a list of commands!')

    @commands.command()
    async def clear(self, ctx, number=10):
        await ctx.channel.purge(limit=number)

    @client.command(aliases=['8ball', '8'])
    async def eightBall(self, ctx, *, question):
        responses = [
            "It is certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes – definitely.",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."]
        await ctx.send(f'**Question:** {question} \n**Answer:** {random.choice(responses)}')


def setup(client):
    client.add_cog(Commands(client))
