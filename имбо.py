import telebot
import random
import logging
from telebot import types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = ""
bot = telebot.TeleBot(TOKEN)

user_data = {}

