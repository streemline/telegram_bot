import telebot
import os
from random import choice
import base_answer
from datetime import datetime
import blacklist
blacklist = blacklist.blacklist
#bit 15.3
clock = datetime.strftime(datetime.now(), "[%H:%M:%S] [%d.%m.%Y]")
print("[######################################]")
print("[ Launched in ",clock)
folder_size = os.path.getsize('base_answer.py')
pod = folder_size/1024
kb = str(pod)
print("[ In base {}kb answer".format(kb[0:3]))
print("[######################################]")

bot = telebot.TeleBot('TOKKEN') #Token bot ==============================================
otvet = base_answer.otvet#slovar
# user 411171602
@bot.message_handler(content_types=['text'])
def send_text(message):
    id_user = (message.from_user.id)#проверка айди
    first_name = (message.from_user.first_name)
    sms = (message.text)#sms

    #Blacklist =============================
    if id_user in blacklist:
        print("[Ignore:{}]".format(id_user))
    elif id_user not in blacklist:
        #Filter sms ========================
        fillter = (",)")
        for char in fillter:
            sms = sms.replace(char,"")

        #Лог файл ===========================
        print("Message: {}, {}".format(first_name, sms))
        logf = open("log.txt", "a", encoding='utf-8')
        logf.write("Message: {}, {}  {} [id:{}]\n".format(first_name,sms,clock,id_user))
        logf.close()

        #Ответ ==============================
        for key in otvet.keys():
            if sms.lower() in key:
                bot.send_message(message.chat.id, "{}, {}".format(first_name,choice(otvet[key])))

bot.polling()