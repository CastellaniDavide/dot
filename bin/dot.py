"""dot
"""
import asyncio
import discord
from dotenv import load_dotenv
from os import getenv

__author__ = "Castellani Davide", "De Battisti Tommaso"
__version__ = "01.01 2021-05-09"

class dot(discord.Client):
    def __init__(self):
        """ Constructor
        """
        super().__init__()
        self.online = {}
        self.locks = {}

    def get_lock(self, server, channel):
        """ Gets the lock
        """
        try:
            return self.locks[server][channel]
        except KeyError:
            self.locks[server] = {}
            self.locks[server][channel] = asyncio.Lock()
        
        return self.locks[server][channel]

    def set_online(self, server, channel, value):
        """ Set online to the given value
        """
        try:
            self.online[server][channel] = value
        except KeyError:
            self.online[server] = {}

        self.online[server][channel] = value

    def get_online(self, server, channel):
        """ Gets the online state
        """
        try:
            return self.online[server][channel]
        except KeyError:
            return False

    async def on_ready(self):
        """ Print a message when online
        """
        print(f"{self.user} has connected to Discord")

    async def on_message(self, message):
        """ Elaboration on each message
        """
        message_string = str(message.content)
        message_guild = str(message.guild.name)
        message_channel = str(message.channel.name)
        message_author = str(message.author.name)

        async with self.get_lock(message_guild, message_channel):
            if message_string == "." and message_author != self.user.display_name:
                self.set_online(message_guild, message_channel, True)
            if message_string.lower() == "carambola":
                self.set_online(message_guild, message_channel, False)

            await asyncio.sleep(1)

            online = self.get_online(message_guild, message_channel)
            if online:
                await message.reply(".")


if __name__ == '__main__':
    load_dotenv()
    dot().run(getenv("DISCORD_TOKEN"))
