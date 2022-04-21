from telebot import TeleBot
from models.analyze import Analyze
from dotenv import load_dotenv
import os

load_dotenv()

token = os.environ['TOKEN']

analyze = Analyze()
bot = TeleBot(token)
