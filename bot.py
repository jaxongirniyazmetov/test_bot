from telegram.ext import Application, CommandHandler, MessageHandler, ConversationHandler, filters
from config import TELEGRAM_TOKEN
from handlers import start, ask_name, ask_age, ask_phone

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            "ASK_PHONE": [MessageHandler(filters.CONTACT, ask_phone)],
            "ASK_NAME": [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_name)],
            "ASK_AGE": [MessageHandler(filters.TEXT & ~filters.COMMAND, ask_age)],
        },
        fallbacks=[],
    )

    app.add_handler(conv_handler)
    app.run_polling()

if __name__ == '__main__':
    main()
