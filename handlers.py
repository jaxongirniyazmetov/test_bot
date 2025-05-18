from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import ContextTypes
from sheets import append_data

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    button = KeyboardButton("Share Contact", request_contact=True)
    reply_markup = ReplyKeyboardMarkup([[button]], one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text("Hi! Please share your phone number:", reply_markup=reply_markup)
    return "ASK_PHONE"

async def ask_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    contact = update.message.contact
    if contact:
        context.user_data['phone'] = contact.phone_number
        await update.message.reply_text("Thanks! What's your name?", reply_markup=ReplyKeyboardRemove())
        return "ASK_NAME"
    else:
        await update.message.reply_text("Please use the button to share your phone number.")
        return "ASK_PHONE"

async def ask_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Great! Now how old are you?")
    return "ASK_AGE"

async def ask_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['age'] = update.message.text
    name = context.user_data.get('name')
    age = context.user_data.get('age')
    phone = context.user_data.get('phone')
    append_data(name, age, phone)
    await update.message.reply_text(f"Thanks {name}! Your data has been saved.")
    return -1
