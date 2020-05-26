from discord.ext import commands # Bot Commands Frameworkのインポート
import discord
import r
import os
prefix = os.environ['DISCORD_BOT_PREFIX']

# コグとして用いるクラスを定義。
class global_chat(commands.Cog):
    # global_chatクラスのコンストラクタ。Botを受取り、インスタンス変数として保持。
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        count=0
        conn=r.connect()
        sm=conn.smembers("gloch")
        for i in sm:
            i=int(i)
            if i==message.channel.id:
                count+=1
        if count>0:
        #発言チャンネルidがsmsに入っていたら反応

            if message.content.startswith(prefix):
                pass
            #発言時、頭にprefixがついていたらpass

            else:
                if message.attachments:
                    for iq in sm:
                        ch=self.bot.get_channel(int(iq))
                        if ch.id == message.channel.id:
                            pass await message.add_reaction("✔️")
                        if message.content:
                            embed = discord.Embed(title=message.content,
                                                  description=None,
                                                  color=0x00bfff)
                            embed.set_author(name=message.author.display_name, 
                                             icon_url=message.author.avatar_url_as(format="png"))
                            embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
                                             icon_url=message.guild.icon_url_as(format="png"))
                            await ch.send(embed=embed)
                        m=0
                        for p in message.attachments:
                            m+=1   
                            embed = discord.Embed(title=f"画像({m})",
                                                  description=None,
                                                  color=0x00bfff)
                            embed.set_image(url=p.url)
                            embed.set_author(name=message.author.display_name, 
                                             icon_url=message.author.avatar_url_as(format="png"))
                            embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
                                             icon_url=message.guild.icon_url_as(format="png"))
                            await ch.send(embed=embed)
                                                                            
                else:
                    await message.delete()
                    embed = discord.Embed(title=message.content,
                                          description=None,
                                          color=0x00bfff)
                    embed.set_author(name=message.author.display_name, 
                                     icon_url=message.author.avatar_url_as(format="png"))
                    embed.set_footer(text=f"{message.guild.name} / {message.channel.name}",
                                     icon_url=message.guild.icon_url_as(format="png"))
                    # Embedインスタンスを生成、投稿者、投稿場所などの設定
                    for iq in sm:
                        ch=self.bot.get_channel(int(iq))
                        await ch.send(embed=embed)
        else:
            await message.channel.send("エラー")                      
                        
def setup(bot):
    bot.add_cog(global_chat(bot))
