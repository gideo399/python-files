from typing import final
from telegram import update
from telegram.ext import Application, CommandHandler, MessageHandler, ContestTypes



TOKEN: Final = '7179935580:AAHzPlUM20RSIdPPxiQorW3wYzTj0R6cdVQ'
BOT_USERNAME : Final = '@DeonTutorial_bot'

#comands 
async def start_command(update :update, ContextTypes.DEFAULT_TYPE)
    await update.message.reply_text("hello Thanks for chatting with me am deon yeh  ")
    
async def help_command(updat :update, ContextTypes.DEFAULT_TYPE)
    await update.message.reply_text("hello Thanks for chatting with me am deon yeh  ")
    
    
async def custom(update :update, ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("This is a custom command ")
    
#responses 

def handle_response(text: str):
    if "hello" in text:
        return "hey there "
    if "How are you" in text:
        return "waguan"
        
    
    
     