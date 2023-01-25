# модуль вывода
import m_import

def view_names():
    array=m_import.read_data()
    for line in array: print(line[1]+" "+line[2])
