from telegram import Update
from telegram.ext import CallbackContext

user_profile = {}

def input_player_name_handler(update: Update, context: CallbackContext) -> None:
    name = update.message.text
    user_profile["name"] = name

    update.message.reply_text(f"Введите возраст:")


def input_player_age_handler(update: Update, context: CallbackContext) -> None:
    age = update.message.text
    update.message.reply_text(f"Вы ввыли age: {age}")