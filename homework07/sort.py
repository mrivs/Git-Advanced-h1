# модуль сортировки
import m_import


def write_array(array):
    with open ("homework07/database.txt","w",encoding="utf8") as data:
        for line in array: 
            s=" ".join(line)
            s+="\n"
            data.write(s)
            

def sorting_id(line):
    n=int(line[0])
    return n
    
def sorting_name(line):
    return line[1]

def sort_id():
    array=m_import.read_data()
    array.sort(key=sorting_id)
    write_array(array)
    m_import.print_data()

def sort_name():
    array=m_import.read_data()
    array.sort(key=sorting_name)
    write_array(array)
    m_import.print_data()

sort_id()        