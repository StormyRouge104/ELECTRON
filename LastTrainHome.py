queues = {}
import asyncio
import discord
import yt_dlp
from discord import app_commands
async def setup (bot):

    @bot.tree.command(name="killerqueen", description ="воспроизвести музишен ред музыкальная шкатулка (ютуб онли)")
    async def kingcrimson(interaction, url:str):
        if interaction.guild.id not in queues: #проверочный очереди
            queues[interaction.guild.id] = []
        await interaction.response.defer(ephemeral= True)
        if not interaction.user.voice:
            await interaction.followup.send("зайди в войс чат мразь сука")
            return
        ludyshki=interaction.guild.voice_client
        if not ludyshki: #проверочный наличия в войсе боба
            ludyshki= await interaction.user.voice.channel.connect() # концовка первого блока с подключением к хуйне
            queues[interaction.guild.id].clear()

# БЛОК ПРОВЕРКИ И АВТОМАТИЧЕКСОГО ЛИВА ПРИ ПУСТОМ ВОЙСЕ

            async def asynccheck():
                while ludyshki.is_connected():
                    await asyncio.sleep(10)
                    check = await interaction.guild.fetch_channel(ludyshki.channel.id)
                    if len(check.members) == 1:
                        queues[interaction.guild.id].clear()
                        await ludyshki.disconnect()
                        break
            asyncio.create_task(asynccheck())

# КОНЦОВКА

            # БЛОК СБОРА ССЫЛОК И ПЛЕЙЛИСТОВ, yt_dlp/ get_url, ПРЯМОЙ АУДИОПОТОК get_stream
        d = {'format': 'bestaudio/best', 'extract_flat':True, 'cookiefile': 'cookies.txt', 'extractor_args': {'youtube': {'player_client': ['web']}}}
        def get_url():
            try:
                ydl = yt_dlp.YoutubeDL(d)
                info = ydl.extract_info(url, download=False)
                if 'entries' in info:
                    for entry in info['entries']:
                        queues[interaction.guild.id].append(entry['url'])
                else:
                    queues[interaction.guild.id].append(url)
            except yt_dlp.utils.DownloadError as e:
                queues[interaction.guild.id].append(str(e))
            # return info['url']
        print("DEBUG\n 1. достаю url")
        idk = await asyncio.to_thread(get_url)
      #queues[interaction.guild.id].append(idk2)
        print("DEBUG\n 2,5. песенка добавлена в очередь")
        def get_stream(web_url):
            if not web_url.startswith("http"):
                return web_url
            try:
                youtuberdl= yt_dlp.YoutubeDL({'format': 'bestaudio/best', 'noplaylist':True, 'cookiefile': 'cookies.txt', 'extractor_args': {'youtube': {'player_client': ['web']}}})
                info= youtuberdl.extract_info(web_url, download=False)
                return info['url']
            except yt_dlp.utils.DownloadError as e:
                return str(e)
        async def asyncnext(): # after=play next принимает только синхронные функции тебе нихуя с этим не поделать нужно отдельную асинхронную хуйню которая возьмёт на себя получение ссылки и запуск произведения
            print("DEBUG\n 2. создаю ffmpeg")
            if not ludyshki.is_connected():
                return
            if queues[interaction.guild.id]:
                current_url = queues[interaction.guild.id][0]
                strimer= await asyncio.to_thread(get_stream, (queues[interaction.guild.id][0]))

                #начало блока проверки ошибок

                if not strimer.startswith("http"):
                    if "playlist does not exist" in strimer:
                        await interaction.channel.send("Ютуб выдал ошибку: плейлист не существует. убедись шо ссылка валидна и/или плейлист открыт в открытый доступ/доступ по ссылке")
                        await interaction.followup.send("Произошла ошибка, детали отправлены в чат")
                    elif "Sign in to confirm your age" in strimer:
                        await interaction.channel.send("Текущая песня имеет ограниченный доступ по возрасту и требует подтверждения возраста по аккаунту, на данный момент это не сделано, будет исправлено в будущем, в следствии чего произведение закончилось. кикните бота с гс или выйдите с гс сами на 10 секунд чтобы сбросить очередь и снова пользоваться ботом ")
                        await interaction.followup.send("Произошла ошибка, детали отправлены в чат")
                    elif "Video unavailable" in strimer:
                        await interaction.channel.send("Ютуб выдал ошибку: текущее видео не существует. убедись шо ссылка валидна и/или видео открыто в открытый доступ/доступ по ссылке ")
                        await interaction.followup.send("Произошла ошибка, детали отправлены в чат")
                    else:
                        await interaction.channel.send(f"Произошла неизвестная ошибка, сообщите о ней сайлу либо через лс либо через команду /report:\n``` {strimer}```")
                        await interaction.followup.send("Произошла ошибка, детали отправлены в чат")

                    queues[interaction.guild.id].pop(0)
                    await asyncnext()
                    return

                #конец блока с ошибками
                queues[interaction.guild.id].pop(0)
                ludyshki.play(discord.FFmpegPCMAudio(strimer,before_options='-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'), after=play_next)
                # интерфейс
                await interaction.channel.send(f"[сейчас играет:]({current_url})")

        def play_next(error): #играть следующего + сбор ошибок
             asyncio.run_coroutine_threadsafe(asyncnext(), interaction.client.loop)
        if not ludyshki.is_playing() and not ludyshki.is_paused():
            await asyncnext()
        else:
            await interaction.followup.send("Я люблю песенку была добавлена")
