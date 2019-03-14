import discord as discord
import random as random

class bot:
    token = '' #remove for public release
    bot = discord.Client()
    class fortunes:
        fortunes = ['yes', 'yes', 'yes', 'no', 'no', 'no', 'maybe', 'possibly', 'its up to you']
    class admin:
        admins = ['438101611022123029']

@bot.bot.event
async def on_message(message) -> None:
    if (message.author != bot.bot.user):
        try:
            queryFinished = False
            if (message.content.startswith('<@{}>'.format(str(bot.bot.user.id)))):
                if (queryFinished != True and message.content.count(' ') >= 1):
                    if (message.content.split(' ')[1] == 'KILLSIG' and str(message.author.id) in bot.admin.admins and queryFinished != True):
                        await bot.bot.send_message(message.channel, 'Bot session was closed by <@{}>.'.format(str(message.author.id)))
                        queryFinished = True
                        exit()
                    elif (message.content.split(' ')[1] == 'KILLSIG' and str(message.author.id) not in bot.admin.admins and queryFinished != True):
                        await bot.bot.send_message(message.channel, 'You dont have permission to do that <@{}>.'.format(str(message.author.id)))
                        queryFinished = True
                    elif (message.content.split(' ')[1].lower() == 'invite' and queryFinished != True):
                        await bot.bot.send_message(message.channel, 'https://discordapp.com/oauth2/authorize?&client_id={}&scope=bot&permissions=325696'.format(bot.bot.user.id))
                        queryFinished = True
                    elif (message.content.split(' ')[1].lower() == 'random-number' and queryFinished != True):
                        try:
                            num1 = int(message.content.split(' ')[2])
                            num2 = int(message.content.split(' ')[3])
                            await bot.bot.send_message(message.channel, 'Choosing a random number from {}-{}...'.format(str(num1), str(num2)))
                            await bot.bot.send_message(message.channel, '{}'.format(str(random.randint(num1, num2))))
                        except Exception:
                            await bot.bot.send_message(message.channel, 'Invalid arguments passed for `random-number`.')
                        queryFinished = True
                if (message.content == '<@{}>'.format(bot.bot.user.id) and queryFinished != True):
                    await bot.bot.send_message(message.channel, '''
```
{} command list:
;;;;conchbot;;;; <question> ? - Gives a random answer; Questions MUST have a question mark at the end.
;;;;conchbot;;;; KILLSIG - Powers off the bot.
;;;;conchbot;;;; random-number <min> <max> - Picks a random number from the range.

If you have any more questions, contact my creator (katznboyz#3144).
```
'''.format(bot.bot.user.name).replace(';;;;conchbot;;;;', '@{}'.format(bot.bot.user.name)))
                    queryFinished = True
                elif (message.content.endswith('?') and queryFinished != True):
                    await bot.bot.send_message(message.channel, str(random.choice(bot.fortunes.fortunes).capitalize()))
                    queryFinished = True
        except Exception as err:
            print (err)

@bot.bot.event
async def on_ready() -> None:
    print ('{} is online!'.format(str(bot.bot.user.name)))
    await bot.bot.change_presence(game = discord.Game(name = '@{}'.format(bot.bot.user.name)))

bot.bot.run(bot.token)

#make it so that it doesnt pick the same answer twice in a row

#TFW you code this at night without comments, wake up the next day, and have no idea what anything does
