# message.from_user.id
# message.from_user.first_name
# message.from_user.last_name
# message.from_user.username


from datetime import datetime as dt
from time import time
def add_log(name,actions):
    time = dt.now().strftime('%H:%M - %d.%m.%Y  ')
    with open('homework10/calclog.txt', 'a') as file:
        string=(time)+" "+name+ " "+actions+"\n"
        file.write(string)