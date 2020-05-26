import os
import r
from discord.ext import commands

class addglobal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def add_global(self, ctx):
        """グローバルチャット登録"""
        cgi=ctx.guild.id
        cci=ctx.channel.id
        ccn=ctx.channel.name
        global_ch="gloch"
        conn=r.connect()
        k=conn.keys()
        gi=str(cgi)
        ci=str(cci)
        count=0
        for i in k: #データベース判定
            if i == gi:
                count+=1
        if count==0: #データベース未登録時
            a1=conn.sadd(cgi,cci)
            a2=conn.sadd(global_ch,cci)
            if a1==True and a2==True:
                embed = discord.Embed(title="**登録情報**", description=None)  
                embed.add_field(name="登録完了", value=f"`登録チャンネル：{ccn}`")
                return await ctx.send(embed=embed)
            else:
                embed = discord.Embed(title="**登録情報**", description=None)  
                embed.add_field(name="登録失敗", value=f"`開発者に問い合わせて下さい`")
                return await ctx.send(embed=embed)

        elif count>0:
            sm=conn.smembers(cgi)
            counts=0
            for ch in sm:      
                if ch == ci:
                    counts+=1
            if counts==0:
                a1=conn.sadd(cgi,cci)
                a2=conn.sadd(global_ch,cci)
                if a1==True and a2==True:
                    embed = discord.Embed(title="**登録情報**", description=None)  
                    embed.add_field(name="登録完了", value=f"`登録チャンネル：{ccn}`")
                    return await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="**登録情報**", description=None)  
                    embed.add_field(name="登録失敗", value=f"`開発者に問い合わせて下さい`")
                    return await ctx.send(embed=embed)
            elif counts>0:
                embed = discord.Embed(title="**登録情報**", description=None)  
                embed.add_field(name="既に登録されています。", value=f"`登録チャンネル：{ccn}`")
                return await ctx.send(embed=embed)

        else:
            embed = discord.Embed(title="**エラー**", description="開発者に問い合わせて下さい")  
            return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(addglobal(bot))
