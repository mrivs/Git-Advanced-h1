
# Прикрутить бота к задачам с предыдущего семинара:
# Создать калькулятор для работы с рациональными и комплексными числами, организовать меню, добавив в неё систему логирования

import telebot
from telebot import types
import random
import modul
import logger
v=0
sign=""
firstval=0
secondval=0
bot = telebot.TeleBot("5622659204:AAEn8RCvePPx-d0oKLzz4n2ApGmFB_gSAWQ") 

def calk(message):
    global firstval,secondval,sign
    res=modul.calculate(firstval,secondval,sign)
    bot.send_message(message.chat.id,f"Результат: {res}")
    name=str(message.from_user.id) +" "+message.from_user.username
    act=str(firstval)+sign+str(secondval)
    logger.add_log(name,act)
    firstval=res
    select_sign(message)

def inp1val(message):
    bot.send_message(message.chat.id,f"Введите 1 значение")
    bot.register_next_step_handler(message,check1val)

def inp2val(message):
    bot.send_message(message.chat.id,f"Введите 2 значение")
    bot.register_next_step_handler(message,check2val)

def check1val(message):
    global firstval,v,secondval
    command=message.text
    if v==1:
        if modul.is_number(command): 
            firstval=float(command)
            select_sign(message)
        else:
            bot.send_message(message.chat.id,f"Неверный формат числа") 
            inp1val(message)
    elif v==2:
        if modul.is_complex(command): 
            firstval=complex(command)
            select_sign(message)
        else:
            bot.send_message(message.chat.id,f"Неверный формат числа") 
            inp1val(message)

def check2val(message):
    global firstval,v,secondval
    command=message.text
    if v==1:
        if modul.is_number(command): 
            secondval=float(command)
            calk(message)
        else:
            bot.send_message(message.chat.id,f"Неверный формат числа") 
            inp2val(message) 
        
    elif v==2:
        if modul.is_complex(command): 
            secondval=complex(command)
            calk(message)
        else:
            bot.send_message(message.chat.id,f"Неверный формат числа") 
            inp2val(message)


def select_sign(message):
    global v
    
    kb=types.InlineKeyboardMarkup(row_width=7)
    btn_summ=types.InlineKeyboardButton("+", callback_data="summ")
    btn_mult=types.InlineKeyboardButton("*", callback_data="mult")
    btn_raz=types.InlineKeyboardButton("-", callback_data="raz")
    btn_del=types.InlineKeyboardButton("/", callback_data="div")
    btn_div_cel=types.InlineKeyboardButton("//", callback_data="div_cel")
    btn_div_ost=types.InlineKeyboardButton("%", callback_data="div_ost")
    btn_cancel=types.InlineKeyboardButton("<--", callback_data="cancel")
    if v==1:kb.add(btn_summ,btn_mult,btn_raz,btn_del,btn_div_cel,btn_div_ost,btn_cancel)
    elif v==2:kb.add(btn_summ,btn_mult,btn_raz,btn_del,btn_cancel)
    bot.send_message(message.chat.id,f"Выберете действие",reply_markup= kb)

def calcNatural(message):
    bot.send_message(message.chat.id,f"calcNatural")

@bot.message_handler(commands = ['start']) 
def start(message):
    
    kb=types.InlineKeyboardMarkup(row_width=1)
    btn1=types.InlineKeyboardButton("действия с натуральными числами", callback_data="calcNatural")
    btn2=types.InlineKeyboardButton("действия с комплексными числами", callback_data="calcComplex")
    kb.add(btn1,btn2)
    bot.send_message(message.chat.id,f"  Калькулятор \n Выберете режим: \n",reply_markup= kb)

@bot.callback_query_handler(func=lambda call: call.data)
def callback_query(call):
    global v,sign
    if call.data == "calcNatural":
        v=1
        inp1val(call.message)

    elif call.data == "calcComplex":
        v=2
        inp1val(call.message)
    
    elif call.data == "summ": 
        sign="+"
        inp2val(call.message)
    elif call.data == "mult":
        sign="*"
        inp2val(call.message)
    elif call.data == "raz":
        sign="-"
        inp2val(call.message)
    elif call.data == "div":
        sign="/"
        inp2val(call.message)
    elif call.data == "div_cel":
        sign="//"
        inp2val(call.message)
    elif call.data == "div_ost":
        sign="%"
        inp2val(call.message)
    elif call.data == "cancel":start(call.message) 
        
        
bot.infinity_polling()       