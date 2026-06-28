import discord
from discord.ext import commands
from discord import app_commands
import json
import datetime
class Embed(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    @app_commands.command(name="add-embed", description="Crée un embed") 
    async def add_embed(self, interaction: discord.Interaction, channel: discord.TextChannel, title: str, description: str, color: str, footer: str):
        json_data = json.load(open("data.json"))
        role_id = int(json_data["embedPermission"])

        if role_id not in [r.id for r in interaction.user.roles]:
            await interaction.response.send_message("Vous n'avez pas la permission d'utiliser cette commande", ephemeral=True)
            return

        hex_color = color.lstrip("#")
        embed = discord.Embed(
            title=title,
            description=description,
            colour=discord.Colour(int(hex_color, 16)) or discord.Colour.random(),
            timestamp=datetime.datetime.now(),
        )

        
        embed.set_footer(text=footer)
        await channel.send(embed=embed)
        await interaction.response.send_message("Embed créé", ephemeral=True)
async def setup(bot):
    await bot.add_cog(Embed(bot))