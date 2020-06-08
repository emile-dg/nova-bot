"""NOVA API for the web and Telegram"""
import logging

from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from api import app, chat_mgr


TOKEN = '1117056414:AAFeReNPaDAwn_9Aat_N7wg1RxgR8LhNjEQ'
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO, filename="nova-log.log", filemode="a")
intro_msg = "Hello, I'm BECCA, your personal assistant. \
                I can help you do some few tasks. Just ask ;)"

def nova_start_t(update, context):
    """Respond to the '/start' command from telegram"""
    context.bot.send_message(chat_id=update.effective_chat.id, text=intro_msg)

def nova_reply_t(update, context):
    """Reply to a telegram client"""
    reply = chat_mgr.respond(update.message.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=reply)

if __name__ == "__main__":
    try:
        telegram_updater = Updater(token=TOKEN, use_context=True)
        telegram_dispatcher = telegram_updater.dispatcher
        # handlers
        reply_handler = MessageHandler(Filters.text & (~Filters.command), nova_reply_t)
        # dispatch handlers
        telegram_dispatcher.add_handler(reply_handler)
        telegram_dispatcher.add_handler(CommandHandler('start', nova_start_t))
        # start telegram polling and the web api
        telegram_updater.start_polling()
        app.run(debug=True)

    except KeyboardInterrupt:
        exit()
