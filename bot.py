import logging


from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
from commands.base import start, player_profile_command
from handlers.player_profile import input_player_name_handler, input_player_age_handler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = "516449158:AAGy7Qki4y1Tpg53ZvPrKV0iTxdPGGmCpo8"



def main() -> None:
    """Start the bot."""

    # Create the Updater and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("player_profile", player_profile_command))
    dispatcher.add_handler(MessageHandler(Filters.text, input_player_name_handler))
    dispatcher.add_handler(MessageHandler(Filters.text, input_player_age_handler))

    # Start the Bot
    updater.start_polling()     # опрашиваем сервер телеграма

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()