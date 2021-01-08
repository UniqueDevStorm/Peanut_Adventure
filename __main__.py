from discord.ext import commands
import discord
import os
from dotenv import load_dotenv
from tools.Autocogs import AutoCogs

load_dotenv(verbose=True)
TOKEN = os.getenv("TOKEN")


class Peanut(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="./")
        self.remove_command("help")
        AutoCogs(self)

    async def on_ready(self):
        print(f"{str(self.user)} 준비 완료.")

    async def on_message(self, message):
        if message.author.bot:
            return
        else:
            await self.process_commands(message)

if __name__ == '__main__':
    Peanut().run(TOKEN, bot=True)