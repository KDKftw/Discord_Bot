import os
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from threading import Thread
from flask import Flask
from discord.utils import get

app = Flask('')
@app.route('/')
def main():
    return "Your bot is alive!"

def run():
    app.run(host="0.0.0.0", port=8080)

def keep_alive():
    server = Thread(target=run)
    server.start()

intents = discord.Intents.default()
intents.members = True

bot = Bot("!", intents=intents)

@bot.event
async def on_ready():
  print("gud 2 go")


@bot.event
async def on_member_join(member):
    print("member join")
    channel = bot.get_channel(929370329363644506)
    #embed=discord.Embed(title="Welcome!",description=f"{member.mention} Just Joined")
    await channel.send(f"{member.mention} Welcome to our server! Please check <#556206910794366988> and set your name and role based on your ingame name and rank. Guide how to change name and rank on discord check <#938095496025759754>")

@bot.command()
@commands.has_permissions(change_nickname=True)
async def nick(ctx, *, nickname):
    member = ctx.author
    await (ctx.message).delete()
    await member.edit(nick=nickname)
    await ctx.send(f"Nickname was changed to {member.mention}.")

@bot.command(pass_context=True)
async def rankZombie(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="Zombie")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankAbom(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="Abomination")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankDS(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="Deathstalker")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankA1(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="A1")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankA3(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="A3")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankDelete(ctx):
  member = ctx.author
  roles = member.roles
  print(roles)
  await (ctx.message).delete()
  await member.edit(roles=[])


keep_alive()



my_secret = os.environ['TOKEN']
bot.run(os.getenv("TOKEN"))