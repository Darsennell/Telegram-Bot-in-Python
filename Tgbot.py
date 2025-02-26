import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Your bot's token
TOKEN = 'YOUR_BOT_TOKEN'

# Set up basic logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Function for the /start command
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Hello! I am a bot. Type /help for assistance.')

# Function for the /help command
def help(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('I can assist with basic commands:\n/start - Greetings\n/help - Help')

def main():
    # Create the Updater object and pass in your bot's token
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))

    # Start polling for updates
    updater.start_polling()

    # Run the bot until you send a signal to stop
    updater.idle()

if __name__ == '__main__':
    main()
