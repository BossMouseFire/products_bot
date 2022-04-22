from telebot import TeleBot
from models.analyze import Analyze
from dotenv import load_dotenv
import os
import yaml

load_dotenv()

token = os.environ['TOKEN']

analyze = Analyze()
bot = TeleBot(token)

with open('config.yaml') as f:
    templates = yaml.safe_load(f)
