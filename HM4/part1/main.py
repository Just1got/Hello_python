# Функция открытия файла
# Params: path - путь к файлу
# Return: считанная строка
def read_file(path):
    f = open(rf'{path}', 'r')
    text = f.read()
    f.close()
    return text

# Функция подсчета с параметрами
# Params: str - строка, splitter - разделители для подсчета, exceptions - исключить символы из строки
# Return: значение подсчета
def counted_with_attribute(str, splitter = None, exceptions = ''):
    text = str.replace('\n', ' ')
    text = text.translate({ord(i): None for i in exceptions})
    if splitter is not None:
        for item in splitter:
            text = text.replace(item, '.')
        text = text.split('.')
        if text[-1] == '':
            text.pop()
    return len(text)

str = read_file("practice-1-main/aristotle.txt")
#str = read_file('practice-1-main/h.txt')

#1. Подсчитывает общее количество символов в файле
print(counted_with_attribute(str))

#2. Подсчитывает общее количесто символов без пробелов
print(counted_with_attribute(str, exceptions = ' '))

#3. Подсчитывает количество символов без знаков препинания
print(counted_with_attribute(str, exceptions = r'.,;:!?-()""'))

#4. Подсчитывает количество слов в файле
print(counted_with_attribute(str, splitter = r' '))

#5. Подсчитывает количество предложений
print(counted_with_attribute(str, splitter = r'.,:!?-()""'))