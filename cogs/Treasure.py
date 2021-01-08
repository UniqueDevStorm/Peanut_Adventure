import discord
from discord.ext import commands


class Treasure(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def 