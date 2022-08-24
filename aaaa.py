from telegram.ext import *
import time

def hl(a,b):
    m =  a.message.reply_text("Hello")
    time.sleep(0.5)
    mm = m.edit_text("Please Wait")
    time.sleep(0.5)
    mm = m.edit_text(mm.text+"\nPleasee......")
    time.sleep(0.5)
    m.edit_text(mm.text+"\nOh Nothing")
    
    print(a.message.from_user)


updater = Updater("5691804740:AAFc1Vvf16R_iYAFJfEFvA_L7HL-p5n1qjk", use_context=True)

updater.dispatcher.add_handler(CommandHandler("start",hl))

updater.start_polling()
updater.idle()
