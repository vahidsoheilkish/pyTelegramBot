

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.chataction import ChatAction
from telegram.ext import CallbackContext, ConversationHandler




def about(update:Update, context:CallbackContext):
    update.message.reply_text("this is about message handle")