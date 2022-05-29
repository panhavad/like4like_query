import logging, os

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import like4like.main as like4like

BOT_TOKEN=os.environ['TELEGRAM_BOT_TOKEN']

# Enable logging
logging.basicConfig(filename='stat.log', filemode='w', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def detail_query(update, context):
    """Send a message when the command /detail is issued."""
    query_id = context.args[0]
    query_res = like4like.fb_page_query(query_id)
    fb_url = 'https://facebook.com/' + query_id
    res_reply = '**' + 'Your request for: ' + fb_url + ' **' + '\n' + 'Current Status: ' + query_res[0]  + '\n' + 'Complete Value: ' + query_res[1]
    update.message.reply_text(res_reply)
    userinfo = update.message.from_user
    logger.info('=== INCOMMING REQUEST ===')
    logger.info('USERNAME: ' + userinfo['username'])
    logger.info('FULLNAME: ' + userinfo['last_name'] + userinfo['first_name'])
    logger.info('ID: ' + str(userinfo['id']))
    logger.info('\n' + res_reply)


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(BOT_TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("detail", detail_query, pass_args=True))
    dp.add_handler(CommandHandler("help", help))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
