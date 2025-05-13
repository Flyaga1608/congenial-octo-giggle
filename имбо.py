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
 task = f"{num1} {op} {num2}"

    if op == '+':
        answer = num1 + num2
    elif op == '-':
        answer = num1 - num2
    elif op == '*':
        answer = num1 * num2
    else:
        answer = num1 // num2

    return task, answer

def create_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("/start"))
    keyboard.add(types.KeyboardButton("/help"))
    keyboard.add(types.KeyboardButton("/score"))
    keyboard.add(types.KeyboardButton("/stop"))
    return keyboard
def start_game(chat_id: int, username: str):
    task, answer = generate_task()
    user_data[chat_id] = {
        'task': task,
        'answer': answer,
        'score': 0,
        'username': username
    }
    bot.send_message(chat_id, f"Привет, {username}! Добро пожаловать в игру по легкой математике.", reply_markup=create_keyboard())
    bot.send_message(chat_id, f"Реши задание:\n{task}\n\nОтправь ответ числом.", reply_markup=create_keyboard())

