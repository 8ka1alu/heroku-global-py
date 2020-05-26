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

        conn=r.connect()
        sm=conn.smembers("gloch")
        sms=str(sm)
        if message.channel.id in sms:
        #発言チャンネルidがsmsに入っていたら反応

            if message.content.startswith(prefix):
                pass
            #発言時、頭にprefixがついていたらpass

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
                for i in sms:
                    ch=self.bot.get_channel(int(sms))
                    await ch.send(embed=embed)
                        
                        
def setup(bot):
    bot.add_cog(global_chat(bot))