import os
from discord.ext import commands
from discord.ext.commands import Bot
from threading import Thread
from flask import Flask
bot = Bot("!")
app = Flask('')

@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()




@bot.command()
@commands.has_permissions(change_nickname=True)
async def nick(ctx, *, nickname):
    member = ctx.author
    await member.edit(nick=nickname)
    await ctx.send(f"Nickname was changed to {member.mention}.")






keep_alive()

my_secret = os.environ['TOKEN']
bot.run(my_secret)