from telegram import Update
from telegram.ext import CallbackContext

user_profile = {}

(
    PLAYER_NAME_STATE,   # 0
    PLAYER_AGE_STATE,    # 1
    PLAYER_GENDER_STATE  # 2
) = range(3)

def input_player_name_handler(update: Update, context: CallbackContext) -> None:
    name = update.message.text
    user_profile["name"] = name

    update.message.reply_text(f"Введите возраст:")
    return PLAYER_AGE_STATE


def input_player_age_handler(update: Update, context: CallbackContext) -> None:
    age = update.message.text
    user_profile["age"] = int(age)
    update.message.reply_text(f"Введите пол:")
    return PLAYER_GENDER_STATE