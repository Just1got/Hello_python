import re


def read_file(path):
    file = open(rf'{path}', 'r')
    text = read_line_to_line(file)
    file.close()
    return text


def read_line_to_line(file):
    i = 0
    error_counter = 0
    for line in file:
        line = convert_data(line, r'^\d*,([\s\S]+?),\d{4}-\d{2}-\d{2},')    #подчищяем запятые в названиях игр
        line = convert_data(line, r'\"(.*?)\",')                            #подчищяем запятые в названии компаний
        x = len(line.split(','))
        if x != 18:
            print(f'a lot if columns ({x} != 18), line {i}')
            error_counter += 1
        i += 1
    print(f'I reed "{file.name}" file. I have {error_counter} errors!')
    return


def convert_data(text, pattern):
    result = re.findall(pattern, text)
    for el in result:
        if result:
            f = el.replace(',', '')
            text = text.replace(el, f, 1)
    return text
