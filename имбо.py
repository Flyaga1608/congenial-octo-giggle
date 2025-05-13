import telebot
import random
import logging
from telebot import types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8122671416:AAGfwP4wLrG-cPeKyv3XVrKxlklIHv99JF8"
bot = telebot.TeleBot(TOKEN)

user_data = {}

