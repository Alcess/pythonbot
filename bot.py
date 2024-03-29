import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix=">")

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('The game of life'))
    print("Bot is ready")

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Beep boop, does not compute. Please pass in all required arguments')
    
@client.command()
async def hello(ctx):
    await ctx.send("Hi There!!!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! {round(client.latency * 1000)}ms")

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["It is certain.",
"It is decidedly so.",
"Without a doubt.",
"Yes - definitely.",
"You may rely on it.",
"As I see it, yes.",
"Most likely.",
"Outlook good.",
"Yes.",
"Signs point to yes.",
"Reply hazy, try again.",
"Ask again later.",
"Better not tell you now.",
"Cannot predict now.",
"Concentrate and ask again.",
"Don't count on it.",
"My reply is no.",
"My sources say no.",
"Outlook not so good.",
"Very doubtful."]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command()
async def clear(ctx, amount=5):
    await ctx.channel.purge(limit=amount)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send('HIKUUUU!')

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)

@client.command()
async def bye(ctx):
    await ctx.send("Sayonara~")

@client.command()
async def hephep(ctx):
    await ctx.send("Hooray!")


client.run("NzYzMjgxODk5MDIzMjM3MTQw.X31bqQ.mTu52gi_Y6dzF3ssYbTr5RXyzSA")
