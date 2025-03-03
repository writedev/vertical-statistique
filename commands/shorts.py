import discord
from discord.ext import commands
from discord import app_commands

class Shorts(commands.Cog):
    def __init__(self, bot : commands.Bot):
        self.bot = bot
        
    @app_commands.command(name="shorts", description="Affiche les informations sur le Youtube Short")   
    async def shorts(self, interaction : discord.Interaction, url : str) -> None:
        
        # verifie que l'url est un lien youtube short
        
        if not url.startswith("https://www.youtube.com/shorts/"):
            embed = discord.Embed(description="L'url doit commencer doit être un lien de partage ** Youtube Short **", color=discord.Color.red())
            return await interaction.response.send_message(embed=embed, ephemeral=True)
            

async def setup(bot):
    await bot.add_cog(Shorts(bot))