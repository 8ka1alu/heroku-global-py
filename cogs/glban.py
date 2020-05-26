from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import asyncio
import datetime

great_owner_id = 459936557432963103

# コグとして用いるクラスを定義。
class bans(commands.Cog):
    # bansクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot
        self.stopcodes = 0

    #gbans a user with a reason
    @commands.command()
    async def gban(self, ctx, user_id: int=None, reason =None):
        """グローバルBan(開発者用)"""
        if ctx.author.id != great_owner_id:
            return
        if reason == None:
            reason = "None"
        for g in self.bot.guilds:
            guildf = self.bot.get_guild(g.id)
            await guildf.ban(discord.Object(user_id), reason=reason)
            await ctx.channel.send(f"{g}からのBANが完了しました。")
            if g == None:
                await self.bot.logout()

    #gunbans a user with a reason
    @commands.command()
    async def gunban(self, ctx, user_id: int=None, reason =None):
        """グローバルUnBan(開発者用)"""
        if ctx.author.id != great_owner_id:
            return
        if reason == None:
            reason = "None"
        for g in self.bot.guilds:
            guildf = self.bot.get_guild(g.id)
            await guildf.unban(discord.Object(user_id), reason=reason)
            await ctx.channel.send(f"{g}からのUNBANが完了しました。")
            if g == None:
                await self.bot.logout()
        
    #bans a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def ban(self, ctx, user_id: int=None, reason =None):
        """Ban(管理者用)"""
        if user_id == None:
            await ctx.channel.send("BAN対象が正しくありません")
            return
        else:
            member = self.bot.get_user(user_id)
            print(member)
        banlog = self.bot.get_channel(694044656501129317)
        if member == ctx.message.author:
            await ctx.channel.send("BAN対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        await ctx.guild.ban(discord.Object(user_id), reason=reason)
        await ctx.channel.send(f"<@{user_id}> をBANしました。")
        await banlog.send(f"BAN通知 \n 鯖名：{ctx.guild.name} \n user id：{user_id} \n 理由：{reason}")
        print(member)

    #unbans a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def unban(self, ctx, user_id: int=None, reason =None):
        """UnBan(管理者用)"""
        if user_id == None:
            await ctx.channel.send("UNBAN対象が正しくありません")
            return
        else:
            member = self.bot.get_user(user_id)
            print(member)
        banlog = self.bot.get_channel(694044656501129317)
        if member == ctx.message.author:
            await ctx.channel.send("UNBAN対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        await ctx.guild.unban(discord.Object(user_id), reason=reason)
        await ctx.channel.send(f"<@{user_id}> をUNBANしました。")
        await banlog.send(f"UNBAN通知 \n 鯖名：{ctx.guild.name} \n user id：{user_id} \n 理由：{reason}")

    #kick a user with a reason
    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def kick(self, ctx, member:discord.User=None, reason =None):
        """Kick(管理者用)"""
        if member == None or member == ctx.message.author:
            await ctx.channel.send("KICK対象が正しくありません")
            return
        if reason == None:
            reason = "None"
        message = f"貴方は{ctx.guild.name}からKICKされました。\n理由:{reason}"
        await ctx.guild.kick(member, reason=reason)
        await member.send(message)
        await ctx.channel.send(f"{member} をKICKしました。")

# Bot本体側からコグを読み込む際に呼び出される関数。
def setup(bot):
    bot.add_cog(bans(bot)) # mainにBotを渡してインスタンス化し、Botにコグとして登録する。
