from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8425167325:AAEOFAnUrC0ul3sKW9gKu0-icrj0LT2tPgk"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("ربات فعاله")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
