import discord
import asyncio
import os
from os.path import join, dirname
from dotenv import load_dotenv

guildID = 0000 # Not set, the guild ID of the server
execRoom = 0000 # Not set, room to post for admin selection
AnnRoom = 0000 # Not set, room to post for public

class MyClient(discord.Client):

    dotenv_path = join(dirname(__file__), '.env')
    load_dotenv(dotenv_path)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.TaskChecker())

    async def TaskChecker(self):
        await self.wait_until_ready()
        i = 0
        while not self.is_closed():
            for file in os.listdir("./images/"):
                await command.AutoEnd(file, client)
                client = self.get_guild(guildID)
                i = i + 1
                if i == 5:
                    break;
            await asyncio.sleep(10)


    async def SubmitPlay(self, content):
        # check how many submissions
        # if already submitted override existing submission.
        # insert / update
        print("submitting play")


    async def RemovePlay(self, content):
        # check to see if a submission is entered
        # remove if there
        # notify what was removed if anything was removed
        print("remove play")


    async def MoveStateOn(self):
        # look at current state and move it to the next state
        print("advancing state")


    async def PostSelection(self):
        # post the current plays to chat
        print("post to exec")


    async def PostToPublic(self):
        # post the current POTM to a public channel to vote.


    async def on_message(self, message):
        prefix = "!!"
        defaultRoom = "agenda"
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return

        if message.content.startswith(prefix + "ping"):
            if command.VerifyRole(message.author.id, message.guild.id, 0):
                await message.author.send("Pong")
                return

        if message.content.startswith(prefix + "submit"):
            print("SUBMIT")

        if message.content.startswith(prefix + "help"):
            print("HELP MENU")

        if message.content.startswith(prefix + "rules"):
            print("rules")

        if message.content.startswith(prefix + "step"):
            print("MOVE STEP ON")



    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')


TOKEN = os.environ.get("DISCORD_BOT_SECRET")
client = MyClient()
client.run(TOKEN)
