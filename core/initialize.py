
from telegram.ext import Updater
import commands.main as commands




class Bot:

    token = "5579731218:AAHObz0By4FN3Xf1bXkuF8m4OgpU_Oa3Vf4"
    api_url = "http://localhost:8000/api"
    web_url = "http://localhost:8000"


    def start(self) -> None:
        updater = Updater(self.token)
        commands.all_commands(updater)
        print("Bot is running...")
        updater.start_polling()
        updater.idle()




bot = Bot()
bot.start()





    