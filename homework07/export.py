# модуль экспорта

def get_new_id():
    with open ("homework07/database.txt","r",encoding="utf8") as data:
        id=max([ int(string[0:string.index(" ")]) for string in data.readlines()])+1
    return str(id) 

def add_data():
    string= get_new_id()
    name= input("введите имя: ")
    sname= input("введите фамилию: ")
    number=input("введите номер: ")
    comment=input("добавте коментарий: ")
    string += " "+name+" "+sname+" "+number+" "+" "+comment  
    with open ("homework07/database.txt","a",encoding="utf8") as data:
        data.write(string+"\n")


    


  
    

