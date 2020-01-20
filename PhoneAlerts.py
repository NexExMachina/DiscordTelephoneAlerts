from twilio.rest import Client
import discord

#print(discord.__version__)  # check to make sure at least once you're on the right version!

# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'TWILIOSID'
auth_token = 'TWILIOTOKEN'
client = Client(account_sid, auth_token)
twinum = '+TWILIOPHONENUMBER'
usernum = '+YOURPHONENUMBER'
ownerid = 'YOURDISCORDUID'
guildid = 'YOURGUILDUID'
#token = open("token.txt", "r").read()  #If we want to use a .txt for token
token = "YOURDISCORDUID"

discclient = discord.Client()  # starts the discord client.

print("Bot Connected")

@discclient.event
async def on_message(message):  # event that happens per any message.  
    print("Waiting for user input")
    if "!alert" in message.content.lower() and message.guild.id == guildid:
        msg_body = message.content.lower().strip("!alert ")
        print(msg_body)
        await message.channel.send('Alerting <@' + str(ownerid) + '>!')
        print(f"{message.channel}: {message.author}: {message.content}")
        call = client.calls.create(
            twiml="<Response><Say>" + str(msg_body) + "...I repeat..." + str(msg_body) + "</Say></Response>",
            to=usernum,
            from_=twinum
            )
        message = client.messages \
                        .create(
                            body = str(msg_body),
                            from_=twinum,
                            to=usernum
                            )
discclient.run(token)  # recall my token was saved!

