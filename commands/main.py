from telegram.ext import MessageHandler,CommandHandler,ConversationHandler
from telegram.ext.filters import Filters
import modules.about.about_functions as about_functions
from variables.about import about_variables


def all_commands(updater):

    updater.dispatcher.add_handler(
        MessageHandler(Filters.regex(about_variables["about"]) , about_functions.about)
    )
