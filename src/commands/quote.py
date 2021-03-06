import discord
from time import time

async def quote_handler(bot:discord.Client, message:discord.Message, command:list, devRole:discord.Role) -> None:
    try:
        ratelimit = 300
        lastcall = int(time() - bot.lastCall["quote"])
        print(ratelimit)
        print(lastcall)
        
        if lastcall <= ratelimit:
            remain = ratelimit - lastcall
            minutes = remain //60
            seconds = remain % 60
            await message.channel.send(f'**{bot.izzymojis["izzyangry"]} RATE LIMIT**\nSorry, but this command has a rate limit to prevent spam. please try again in `{minutes} Minutes {seconds} Seconds`')
            return

        else:
            response = await bot.inspirobot.get_quote()
            e = discord.Embed(colour=0xff00e7, title="Quote from Inspirobot")
            e.set_image(url=response)
            
            await message.channel.send(embed=e)
            bot.lastCall["quote"] = time()
    # NO NO NO NO, WHY U DO DIS???
    except Exception as e:
        await message.channel.send(f"**{bot.izzymojis['izzyangry']} IZZY**\nHey {devRole.mention} There was an error.\n```\n{e}\n```")
