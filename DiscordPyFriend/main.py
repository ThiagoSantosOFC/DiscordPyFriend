from http import client
import discord
import os 
from dotenv import load_dotenv
from neuralintents import GenericAssistant

chatbot = GenericAssistant()

client = discord.Client()

load_dotenv()

TOKEN = os.getenv('TOKEN')

async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$PyFriend'):
        pass
        

client.run (TOKEN)