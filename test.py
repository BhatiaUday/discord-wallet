from discord.ext import commands
from discord import app_commands, Intents, Client, Interaction

bot = commands.Bot(intents=Intents.none(),command_prefix="!")

@commands.cooldown(rate=1, per=5, type=commands.BucketType.user)
@bot.command()
async def example(ctx):
    await ctx.send("Command received ")

bot.run("TOKEN")