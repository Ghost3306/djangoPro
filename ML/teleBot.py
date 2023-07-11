import telegram.ext
import telegram
from teleML import response
def start(update, context):
    update.message.reply_text("Hello! Welcome to Content Recommendation System.")
    update.message.reply_text("Myself Aura your virtual asistent to guide you.")
    
def help(update,context):
    update.message.reply_text("""
    The following commands are avilable:
    
    /start -> Welcome to the channel
    /help -> This message
    /contact -> contact information 
     """)
 
def contact(update, context):
    update.message.reply_text("Our email is aura@25gmail.com")

def send_msg(update,context,str):
    update.message.reply_text(str)
    return update.message.text


def handle_message(update, context):
    data = response(update.message.text)
    update.message.reply_text(data)



Token = ("6123874529:AAHYHEuJky9M8HmQZiWIASchx_wqGVmvjkQ")
#print(bot.get_me())
updater = telegram.ext.Updater("6123874529:AAHYHEuJky9M8HmQZiWIASchx_wqGVmvjkQ", use_context=True)
disp = updater.dispatcher

disp.add_handler(telegram.ext.CommandHandler('start',start))
disp.add_handler(telegram.ext.CommandHandler('help',help))
disp.add_handler(telegram.ext.CommandHandler('contact',contact))
disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()