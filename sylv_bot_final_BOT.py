import os


import discord
from discord.ext import commands
from discord.ext.commands import Bot
from threading import Thread
from flask import Flask







app = Flask('')
@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()


client = discord.Client()
@client.event
async def on_member_join(member):
    print("member join")
    channel = client.get_channel(929370329363644506)
    #embed=discord.Embed(title="Welcome!",description=f"{member.mention} Just Joined")
    await channel.send(f"{member.mention} Welcome to our server! Please check <#556206910794366988> and set your name and rank based on your ingame name and rank")

bot = Bot("!")
@bot.command()
@commands.has_permissions(change_nickname=True)
async def nick(ctx, *, nickname):
    member = ctx.author
    await member.edit(nick=nickname)
    await ctx.send(f"Nickname was changed to {member.mention}.")






keep_alive()

my_secret = os.environ['TOKEN']
bot.run(my_secret)