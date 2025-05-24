from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def di_hola(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Es un gusto interactuar contigo")

aplicacion = ApplicationBuilder().token("7909343554:AAGEfIPlRIV5X2TMcRfOM1X3867-M7f16Ns").build()
aplicacion.add_handler(CommandHandler("start", di_hola ))
aplicacion.add_handler(CommandHandler("echo", echo))

aplicacion.run_polling(allowed_updates=Update.ALL_TYPES)