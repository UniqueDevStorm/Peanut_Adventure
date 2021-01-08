import discord
from discord.ext import commands
import asyncio
import random


class Treasure(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="탐험")
    async def Adventure(self, ctx):
        a = await ctx.send("탐험중.")
        await asyncio.sleep(1)
        await a.edit(content="탐험중..")
        await asyncio.sleep(1)
        await a.edit(content="탐험중...")
        await asyncio.sleep(1)
        r = random.randint(1, 2)
        if int(r) == 1:  # 상자 발견
            await a.edit(content="상자를 발견하셨습니다!")
        elif int(r) == 2:  # 몬스터 ㅎㅇ
            await a.edit(content="님 몬스터 발견")


def setup(bot):
    bot.add_cog(Treasure(bot))
    print("Treasure.py 준비 완료.")
