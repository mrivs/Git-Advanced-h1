# модуль импорта

def read_data():
    with open ("homework07/database.txt","r", encoding="utf8" ) as data:
        
        li=data.readlines()
        array= [st.split() for st in li]
    return array

def print_data(): 
    with open ("homework07/database.txt","r", encoding="utf8" ) as data:
        print(data.read())

        
