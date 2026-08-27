import discord
from discord import app_commands
async def setup (bot):

    @bot.tree.command(name="votestage1", description ="голосовать в 104 авардсах")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels= True)
    async def stage1(interaction):
