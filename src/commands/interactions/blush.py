import discord


async def handler(bot: discord.Client, message: discord.Message, command: list, devRole: discord.Role) -> None:
    response = f'{message.author.display_name} blushes'

    e = discord.Embed(colour=0xff00e7, title=response)
    e.set_image(url=await bot.tenor.get_interact("anime blush"))
    await message.channel.send(embed=e)