import telegram.ext
import telegram
from telegram.ext import MessageHandler,Filters
from teleML import *

from rawMLdata import *
data_file=open('intents.json').read()
intents=json.loads(data_file)
model = load_model('mymodel.h5')

def get_msg(text):
    return_list=predict_class(text,model)
    if len(return_list)==0:
        tag='noanswer'
    else:    
        tag=return_list[0]['intent']
    
    list_of_intents= intents['intents']    
    for i in list_of_intents:
        if tag==i['tag'] :
            result= random.choice(i['responses'])
    return result


def start(update, context):
    update.message.reply_text("Hello! Welcome to Student Support Chatbot System.")
    update.message.reply_text("Myself Aura your virtual asistent to guide you.")
 
def get_var(update,context):
    data = update.message.text
    return data

def handle_message(update, context):
    data = update.message.text
    #s = get_tag(data)
    #print(s)
    ret = response(data)
    update.message.reply_text(ret)
    tag = predict_class(data,model)
    time.sleep(1)
    
    if(tag[0]['intent']=="register"):
        update.message.reply_text("Enter your name : ")
        name = get_var()
    else:
        print("")

    print(name)

Token = ("6123874529:AAHYHEuJky9M8HmQZiWIASchx_wqGVmvjkQ")
updater = telegram.ext.Updater("6123874529:AAHYHEuJky9M8HmQZiWIASchx_wqGVmvjkQ", use_context=True)
disp = updater.dispatcher
echo_handler =MessageHandler(Filters.text,handle_message)
disp.add_handler(echo_handler)
disp.add_handler(telegram.ext.CommandHandler('start',start))
#disp.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, handle_message))
updater.start_polling()
updater.idle()