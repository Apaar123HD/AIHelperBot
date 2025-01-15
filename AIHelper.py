#importing all the modules
import discord
from discord.ext import commands
import google.generativeai as genai

genai.configure(api_key="gemini key")
model = genai.GenerativeModel("gemini-1.5-flash")

#configuring discord intents
intents = discord.Intents.all()
intents.message_content = True

#creating client
client = commands.Bot(intents=intents, command_prefix=',', case_insensitive=True)

#ping command
@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms is your ping ')

#making sure it has turned on
#changing it's status
@client.event
async def on_ready():
    await client.tree.sync()
    print(f'We have logged in as {client.user}')
    await client.change_presence(status=discord.Status.online, activity=discord.Activity(name="prefix is ','"))

#the command to get help from AI
@client.command()
async def helpme(ctx):
    msg_content = ctx.message.content
    msg_reply = model.generate_content(f"respond to this IN LESS THAN 2000 CHARACTERS: {msg_content}")
    await ctx.reply(msg_reply.text)



#actually running the discord bot using the key
client.run("discord key")
