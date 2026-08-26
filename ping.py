async def setup (bot):
    import discord
    from discord import app_commands

    @bot.tree.command(name="ping", description ="Показывает яйца но с точностью в ,kznm cerf")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=True)
    async def ping(interaction):
        ms = round(bot.latency * 1000)
        await interaction.response.send_message(str(ms) + "мс", ephemeral= True)
