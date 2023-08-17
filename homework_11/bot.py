import os
import telebot
from telebot import types
from dotenv import load_dotenv
from send_request import send_request
from send_request import return_urls
from os.path import join, dirname

dotenv_path = join(dirname(__file__), ".env")
load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", " ")

bot = telebot.TeleBot(BOT_TOKEN)


languages = {
    "English": "eng",
    "Українська": "uk",
}
MIN_NUM, MAX_NUM = 1, 50
ENG_TEXT: dict = {
    "question": "What gif you want to find?",
    "limit": "How many do you want to see?",
    "instructions": f"Input a number in range {MIN_NUM}-{MAX_NUM}.",
    "num_error": "WRONG number. Please try again!",
}

UKR_TEXT: dict = {
    "question": "Яку гіфку ти шукаєш?",
    "limit": "Скільки ти хочеш побачити?",
    "instructions": f"Введіть число в діапазоні {MIN_NUM}-{MAX_NUM}.",
    "num_error": "НЕПРАВИЛЬНИЙ номер. Спробуйте ще раз!",
}


def start_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True)
    English = types.KeyboardButton(text=languages.get("English", ""))
    Ukrainian = types.KeyboardButton(text=languages.get("Українська", ""))
    keyboard.add(English, Ukrainian)
    keyboard.one_time_keyboard = True
    return keyboard


@bot.message_handler(commands=["start", "hello", "language"])
def lang_handler(message):
    text = f"Choose language/Обери мову\n"
    sent_msg = bot.send_message(message.chat.id, text, reply_markup=start_keyboard())
    bot.register_next_step_handler(sent_msg, query_handler)


def make_lang_choice(message):
    choice: dict = dict()
    if message == languages.get("English"):
        choice = ENG_TEXT
    if message == languages.get("Українська"):
        choice = UKR_TEXT
    return choice


def query_handler(msg):
    lang = msg.text
    choice = make_lang_choice(lang)
    text = choice["question"]
    query = bot.send_message(msg.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(query, limit_handler, lang)


def limit_handler(msg, lang_msg):
    query = msg.text
    lang = lang_msg
    choice = make_lang_choice(lang_msg)
    text = choice["limit"] + choice["instructions"]
    limit = bot.send_message(msg.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(limit, fetch_query, query, lang)


def fetch_query(limit, query, lang):
    l = limit.text
    req = send_request(lang, query, l)
    data = return_urls(req)
    list = []
    for i, img in enumerate(data, start=1):
        url, title = img
        list.append(f"{i}: {title}:" + f"    {url}\n")

    bot.send_message(limit.chat.id, "Here's your GIFs!")
    for el in list:
        bot.send_message(limit.chat.id, el, parse_mode="Markdown")


bot.infinity_polling()
