import discord 
import os
import asyncio

#トークン
TOKEN = os.environ['DISCORD_BOT_TOKEN']

# 接続に必要なオブジェクトを生成
client = discord.Client()

#起動メッセージ
@client.event
async def on_ready():
    print("起動しました")

@client.event
async def on_message(message):

    if 'Bumpを確認しました' in message.content:
        await message.channel.send('bumpを確認しました！2時間後お願いします！') 
        await asyncio.sleep(7200)
        await message.channel.send('bumpチャンス！') 

    if message.author == message.guild.me:
        return

client.run(TOKEN)

#ノア
#グローバルチャット
#1
