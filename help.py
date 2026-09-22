import discord
from discord import app_commands
class Golosovanie (discord.ui.Modal):# !!!!! ПЕРВЫЙ КЛАСС (22.09.26 чё это нахуй должно значить?????)
    def __init__(self):
        super().__init__(title="Доложить о проблеме с ботом")
        self.sho = discord.ui.TextInput(label="шо случилось", style=discord.TextStyle.paragraph, placeholder="мразь бобейн сломал бота и музыка не робит")
        self.wathapend = discord.ui.TextInput(label="ещё информация", style=discord.TextStyle.paragraph, placeholder="скриншоты/ссылки на сообщения, что делали после чего случилось")
        self.add_item(self.sho)
        self.add_item(self.wathapend)
    async def on_submit(self, interaction):
        await interaction.response.defer(ephemeral=True)
        results = await interaction.client.fetch_user(1137764637794893856)
        await results.send(f" REPORT\n што случилось - {self.sho.value}\n больше инфы - {self.wathapend.value}\n от {interaction.user.mention}")
        await interaction.followup.send("Репорт был отправлен\n (если вы это читаете, передайте ване бобейну что он любит игру в кальмара)", ephemeral=True)
async def setup (bot):

    @bot.tree.command(name="help", description ="инфо и команды")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels= True)
    async def helpa(interaction):
        await interaction.response.send_message("# ШО Я УМЕЮ\n 1. help - хелпа\n 2. ping - пинг сервера/бота + узнать версию бота (чисто для дебага)\n 3. pic - поиск изображений как в телеграме (почти) (***!!! НЕ РОБИТ !!!***)\n 4. report - сообщить о проблеме с ботом/предложить что-то\n 5. killerqueen - играть музыку чисто с ютуба и ютуб мьюзик т.к другие боты сдохли изза проблем с АП и прочим\n 6. vote - ????\n\n### вы можете участвовать в программе тестирования бота, напишите сайлу и вы получите (скорее всего) доступ к экслюзивному серверу и экслюзивному 104 боту - BITZ104_real", ephemeral= True)


    #report


    @bot.tree.command(name="report", description ="доложить о яйцах (проблеме)")
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels= True)
    async def reporter(interaction):
        await interaction.response.send_modal(Golosovanie())


