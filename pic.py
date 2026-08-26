import discord
from discord import app_commands
async def setup (bot):

    @bot.tree.command(name="pic", description ="Выбор изображений як в телеге только дискордчанский")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels= True)
    async def pic(interaction):
        await interaction.response.send_message("# команда временно не работает т.к бот переписывается с джаваскрипта на пайтон. команда является заглушкой на данный момент времени", ephemeral= True) # сука не забывай что ephemereral это локальная отправка
