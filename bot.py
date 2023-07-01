import discord
import responses
import main

async def send_message(message, user_message):

    processed_msg = user_message.lower()

    if processed_msg == '!silence':
        if main.silent == True:
            await message.channel.send('I am already silenced!')
            return
        else:
            main.silent = True
            await message.channel.send('I will now be quiet!')
            return

    if processed_msg == '!speak':
        if main.silent == False:
            await message.channel.send('I can already speak! ^^')
            return
        else:
            main.silent = False
            await message.channel.send('I CAN FINALLY SPEAK AGAIN, THANK YOU! :D <3')
            return

    if main.silent == False:
        try:
            response = responses.get_response(processed_msg)
            await message.channel.send(response)
        except Exception as ex:
            print(ex)


async def send_private_message(message):
    await message.author.send('Psst...Hey who are we hiding from? I promise the I won\'t tell anyone what you said here')


def run_discord_bot():
    BOT_TOKEN = 'MTEyNDM3MTgzMjEwODIyMDU3Ng.G5VL5W.SxPAHFat2m12l8hTlIpqkWc5fkvbcp6ulCGOnY'
    client = discord.Client(intents=discord.Intents.all())

    @client.event
    async def on_ready():
        #Tells server is running
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        #client.user is bot so it won't get stuck infinitely
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            #Read message without '?' in beginning
            user_message = user_message[1:]
            await send_private_message(message)
        else:
            await send_message(message, user_message)

    


    client.run(BOT_TOKEN)
