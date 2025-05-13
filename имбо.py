import telebot
import random
import logging
from telebot import types

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = ""
bot = telebot.TeleBot(TOKEN)

user_data = {}

def generate_task():
    operations = ['+', '-', '*', '/']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    op = random.choice(operations)

    if op == '/':
        num1 = num1 * num2  


