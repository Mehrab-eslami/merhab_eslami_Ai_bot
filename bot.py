import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters
from ai_api import ask_gpt
from db import save_message

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "7856145246:AAGdMTzjmX_P_ntVa_bE2_sv3IzR3ZhlRG0"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_message = update.message.text
    save_message(user_id, "user", user_message)

    reply = ask_gpt(user_message)
    save_message(user_id, "bot", reply)
    await update.message.reply_text(reply)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()