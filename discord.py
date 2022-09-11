#embed=discord.Embed(title="Welcome!",description=f"{member.mention} Just Joined")

## embdem vypada fancy msg

bot = Bot("!")

@bot.command()
@commands.has_permissions(change_nickname=True)
async def nick(ctx, *, nickname):
    member = ctx.author
    await member.edit(nick=nickname)
    await ctx.send(f"Nickname was changed to {member.mention}.")