import os
import asyncio

import discord
import youtube_dl
from discord.ext import commands
from youtube_search import YoutubeSearch

ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': './ffmpeg/windows/bin/ffmpeg.exe'
} if os.name == 'nt' else {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg_location': 'linux here'
}

class music(commands.Cog):
    def __init__(self, bot: discord.Client):
        self.bot = bot

    @commands.command(name='play')
    async def play(self, ctx: discord.ext.commands.Context, *args):
        player = Player.get_or_start_player(ctx)
        player.add_song(' '.join(args))
        await player.play()

    @commands.command(name='playlist')
    async def play_list(self, ctx: discord.ext.commands.Context):
        await Player.get_or_start_player(ctx).print_playlist()

    @commands.command(name='skip')
    async def skip(self, ctx: discord.ext.commands.Context):
        await Player.get_or_start_player(ctx).skip()

    @commands.command(name='pause')
    async def pause(self, ctx: discord.ext.commands.Context):
        Player.get_or_start_player(ctx).pause()

    @commands.command(name='resume')
    async def resume(self, ctx: discord.ext.commands.Context):
        Player.get_or_start_player(ctx).resume()

def setup(bot):
    bot.add_cog(music(bot))

class Song():
    def __init__(self, keyword):
        self.infodict = YoutubeSearch(keyword, max_results=1).to_dict()[0]

    def get_full_url(self):
        return "https://youtube.com/" + self.infodict['url_suffix']

    def get_short_title(self):
        short_title = self.infodict['title'][:45] + "..." if len(self.infodict['title']) > 50 else self.infodict['title']
        return short_title

class Player():
    players = []

    def __init__(self, ctx):
        self.ctx = ctx
        Player.players.append(self)
        self.guild_id = ctx.guild.id
        self.playlist = []
        self.playing = False

    @staticmethod
    def get_or_start_player(ctx):
        for i in Player.players:
            if i.guild_id == ctx.guild.id:
                return i
        else:
            return Player(ctx)

    async def play(self):
        self.playing = True
        await self.play_next_song()

    def resume(self):
        if not self.playing:
            self.playing = True
            self.ctx.voice_client.resume()

    def pause(self):
        if self.playing:
            self.playing = False
            self.ctx.voice_client.pause()

    def add_song(self, keyword):
        self.playlist.append(Song(keyword))

    async def play_next_song(self):
        playlist = self.playlist
        ctx = self.ctx
        if len(playlist) > 0:
            song = playlist[0].get_full_url()
            channel = ctx.message.author.voice.channel

            if ctx.voice_client is None:
                vc = await channel.connect()
            path = './music/' + str(ctx.message.guild.id) + '.mp3'
            if os.path.exists(path):
                os.remove(path)

            ydl_opts['outtmpl'] = path
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                file = ydl.extract_info(song, download=True)

            playlist.pop(0)

            ctx.voice_client.play(discord.FFmpegPCMAudio(path, executable=ydl_opts['ffmpeg_location']))
            ctx.voice_client.source = discord.PCMVolumeTransformer(ctx.voice_client.source, 1)
            while ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                await asyncio.sleep(0.1)
            await self.play_next_song()

        else:
            await ctx.voice_client.disconnect()
            self.playing = False

    async def print_playlist(self):
        ctx = self.ctx
        playlist = self.playlist
        if len(playlist) > 0:
            embed = discord.Embed(title="Current playlist:")
            songlist = ""
            for i in playlist:
                with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                    video_title = i.get_short_title()
                    songlist += "- " + video_title + "\n"
            embed.add_field(name="Songs:", value=songlist, inline=False)
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="No songs in playlist!")
            await ctx.send(embed=embed)

    async def skip(self):
        self.ctx.voice_client.stop()
        embed = discord.Embed(title="Skipped song")
        await self.ctx.send(embed=embed)