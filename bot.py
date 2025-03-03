from discord.ext import commands
import discord
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="!", intents=discord.Intents.all())
    
    """chargements des commandes et des évènements"""
    
    async def setup_hook(self):
        
        for filename in os.listdir("./commands"):
            if filename.endswith(".py"):
                await self.load_extension(f"commands.{filename[:-3]}")

        for filename in os.listdir("./events"):
            if filename.endswith(".py"):
                await self.load_extension(f"events.{filename[:-3]}")
    
    """chargements dans app commands"""
    
    async def setup_hook(self):
        await self.tree.sync()
    

bot = MyBot()

bot.run(TOKEN)
