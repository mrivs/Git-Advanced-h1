
import telebot
from telebot import types
import random
bot = telebot.TeleBot("...") 
Konf=221
pl=1
max=28
def status(message,N,pl):bot.send_message(message.chat.id,f"Конфет осталось: {N}. Ходит игрок {pl}:")

def input_2p(message):
    bot.register_next_step_handler(message,two_payers_game)

def input_1p(message):
    bot.register_next_step_handler(message,bot_game)

def change_pl(pl):
    if pl==1:pl=2
    else:pl=1
    return pl

def two_payers_game(message):
    global Konf,pl
    command=message.text
    if command=="q" or command=="Q":
        bot.send_message(message.chat.id,f"Игра прервана")
        start(message)

    else:
        if command.isdigit():
            count=int(command)
            if 0< count <29: 
                Konf=Konf-count
                if -30<Konf<1:
                    bot.send_message(message.chat.id,f"ИГРОК {pl} ВЫЙГРАЛ!!")
                    start(message)
                else:
                    pl=change_pl(pl)
                    status(message,Konf,pl)
                    input_2p(message)   
            else:
                bot.send_message(message.chat.id,f"введите число конфет от 1 до 28") 
                input_2p(message)
        else: 
            bot.send_message(message.chat.id,f"введите число конфет от 1 до 28") 
            input_2p(message)       

def pc_take_sweet(message):
    global Konf,pl
    value=Konf%(29)
    if value==0:value=random.randint(1, 28)
    Konf=Konf-value
    bot.send_message(message.chat.id,f" Бот забирает {value} конфет  ")
    if -30<Konf<1:
                bot.send_message(message.chat.id,f"БОТ ВЫЙГРАЛ!!")
                start(message)
    else:
        status(message,Konf,"человек")
        input_1p(message)  

def bot_game(message):
    global Konf,pl
    
    command=message.text
    if command=="q" or command=="Q":
        bot.send_message(message.chat.id,f"Игра прервана")
        start(message)
    else: 
        if command.isdigit():
            count=int(command)
            if 0< count <29: 
                Konf=Konf-count
                if -30<Konf<1:
                    bot.send_message(message.chat.id,f"Человек ВЫЙГРАЛ!!")
                    start(message)
                else:
                    pl=change_pl(pl)
                    
                    pc_take_sweet(message)   
            else:
                bot.send_message(message.chat.id,f"введите число конфет от 1 до 28") 
                input_1p(message)
        else:
                bot.send_message(message.chat.id,f"введите число конфет от 1 до 28") 
                input_1p(message)

@bot.message_handler(commands = ['start'])  #вызов функции по команде в списке
def start(message):
    bot.send_message(message.chat.id,f"  Приветствую в игре в конфеты! \n Выберете режим: \n"
    " Два игрока: /startTwoPlayers \n Игра против бота: /startWithPC \n прервать игру: q ")

@bot.message_handler(commands = ['startTwoPlayers'])  #вызов функции по команде в списке
def startTwoPlayers(message):
    global Konf,pl
    pl=random.randint(1, 2)
    Konf=221
    bot.send_message(message.chat.id,f"  Режим игрок против игрока \n Первый ходит игрок {pl}")
    status(message,Konf,pl)
    input_2p(message)
            
@bot.message_handler(commands = ['startWithPC'])  #вызов функции по команде в списке
def startWithPC(message):
    global Konf,pl
    pl=random.randint(1, 2)
    Konf=221
    
    if pl==1:
        bot.send_message(message.chat.id,f"  Режим игрок  против бота \n Первый ходит Человек")
        status(message,Konf,"человек")
        input_1p(message)
    else:
        bot.send_message(message.chat.id,f"  Режим игрок  против бота \n Первый ходит Бот!")
        
        pc_take_sweet(message)

bot.infinity_polling()


