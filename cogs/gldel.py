import os
import r
from discord.ext import commands
import discord

class delglobal(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(manage_guild=True)
    async def del_global(self, ctx):
        """グローバルチャット登録解消"""
        cgi=ctx.guild.id
        cci=ctx.channel.id
        ccn=ctx.channel.name
        global_ch="gloch"
        conn=r.connect()
        k=conn.keys()
        gi=str(cgi)
        ci=str(cci)
        count=0
        for i in k: 
            if i == gi:
                count+=1
        if count==0: 
            embed = discord.Embed(title="**エラー**", description="登録がされていない鯖です")  
            return await ctx.send(embed=embed)

        elif count>0:
            sm=conn.smembers(cgi)
            counts=0
            for ch in sm:      
                if ch == ci:
                    counts+=1
            if counts==0:
                embed = discord.Embed(title="**エラー**", description="このチャンネルは登録されていません")  
                return await ctx.send(embed=embed)
            elif counts>0:
                a1=conn.srem(cgi, cci)
                a2=conn.srem(global_ch, cci)
                if a1==True and a2==True:
                    embed = discord.Embed(title="**登録解消情報**", description=None)  
                    embed.add_field(name="登録を解消しました", value=f"`登録チャンネル：{ccn}`")
                    return await ctx.send(embed=embed)
                else:
                    embed = discord.Embed(title="**エラー**", description="開発者に問い合わせて下さい")  
                    return await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title="**エラー**", description="開発者に問い合わせて下さい")  
            return await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(delglobal(bot))
