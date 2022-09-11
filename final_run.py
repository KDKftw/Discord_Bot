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
    channel = bot.get_channel(861209420448661564) ##welcome channel
    #embed=discord.Embed(title="Welcome!",description=f"{member.mention} Just Joined")
    ##first id Rules channel ; second id is bot commands
    await channel.send(f"{member.mention} Welcome to our server! Please read our rules here <#936600918500180049> and set your name and role based on your ingame name and rank. How to change name and role on discord check <#938395744891723797> . Have fun!")

@bot.command()
@commands.has_permissions(change_nickname=True)
async def nick(ctx, *, nickname):
    member = ctx.author
    await (ctx.message).delete()
    print("nick change")
    await member.edit(nick=nickname)
    ##await ctx.send(f"Nickname was changed to {member.mention}.")

@bot.command(pass_context=True)
async def rankZombie(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="Zombie")
  print("rank zombie")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankAbom(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="Abomination")
  print("rank abom")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankDS(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="Deathstalker")
  print("rank DS")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankA1(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="A1")
  print("rank A1")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankA3(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="A3")
  print("rank A3")
  await member.add_roles(role)


@bot.command(pass_context=True)
async def rankKD(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="KILL DRAGON")
  print("rank KD")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankPVP(ctx):
  member = ctx.author
  await (ctx.message).delete()
  role = get(member.guild.roles, name="PvP")
  print("rank PVP")
  await member.add_roles(role)

@bot.command(pass_context=True)
async def rankDelete(ctx):
  member = ctx.author
  roles = member.roles
  print(roles)
  await (ctx.message).delete()
  print("rank delete")
  await member.edit(roles=[])


keep_alive()



#my_secret = os.environ['TOKEN2']
bot.run(TOKEN)