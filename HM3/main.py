# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#1) Из строки «Python is the best programming language in the world» получить подстроку начиная с 6 символа с начала
# исходной строки и до 7 символа с конца исходной строки (нумерация символов начинается с нуля).
s = "Python is the best programming language in the world"
print(s[6:-7])

#2) Вывести каждый третий символа строки «Guido van Rossum is the benevolent dictator for life».
print("Guido van Rossum is the benevolent dictator for life"[::3])

#4) Из строки «You have a problem with authority, Mr. Anderson.» получить словарь, где ключ -это символ, а значение -
# это количество повторений символа в строке.
s = "You have a problem with authority, Mr. Anderson."
g = dict(zip(list(s), list(map(s.count,list(s)))))
print(g)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
