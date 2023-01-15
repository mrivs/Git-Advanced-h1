# 38. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".(Задание из семинара)


text = "ааабваа! аааа, аабв вввв. Абв ггг"
text_list = text.split()
result = list(filter(lambda x: not "абв" in x.lower() ,text_list))
print(result)