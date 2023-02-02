import read_my_file

def counted_with_attribute(str, splitter = None, exceptions = ''):
    text = str.replace('\n', ' ')   #заменим перенос строки на пробелы. Абзацы считать не будем
    text = text.translate({ord(i): None for i in exceptions})   #удаляем все элементы exceptions
    if splitter is not None:
        for item in splitter:
            text = text.replace(item, '.')
        text = text.split('.')
        text = [el for el in text if el != '']   #удаляем все пустые элементы
    return len(text)

str = read_my_file.read_file("practice-2-main/steam.csv")
#str = read_my_file.read_file("practice-2-main/test")