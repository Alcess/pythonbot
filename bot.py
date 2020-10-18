import discord
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    print("Bot is ready")

@client.command()
async def hello(ctx):
    await ctx.send("Hi")

client.run("NzYzMjgxODk5MDIzMjM3MTQw.X31bqQ.mTu52gi_Y6dzF3ssYbTr5RXyzSA")
