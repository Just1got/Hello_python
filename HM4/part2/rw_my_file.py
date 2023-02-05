import re


def read_file(path):
    file = open(rf'{path}', 'r')
    maps = read_line_to_line(file)
    file.close()
    return maps


def read_line_to_line(file):
    error_counter = 0
    # start reading from line 2
    head = file.readline().rstrip().split(',')
    hash_dict_ = {}                             #хэш для быстрого поиска по параметрам строк { param { param : list(id_game)}}
    games_ = {}                                 #хранит все данные { id_game : list(line)}
    for i in head:
        hash_dict_[i] = {}
    i = 1
    for line in file:
        line = parsing_line(line.rstrip(), r'"(.*?)"[\,|\n]', ',')   #учитываем запятые в кавычках
        if len(line) != 18:
            print(f'error split columns ({len(line)} != 18), line {i}')
            error_counter += 1
            i += 1
            continue
        games_[line[0]] = ','.join(str(el) for el in line)
        for k in range(len(line)):
            for el in line[k].split(';'):
                if not hash_dict_[head[k]].__contains__(el):
                    hash_dict_[head[k]][el] = []
                hash_dict_[head[k]][el].append(line[0])
        i += 1
    print(f'I reed {len(games_)} items from "{file.name}" file. I have got {error_counter} errors!')
    return (games_, hash_dict_)


def parsing_line(text, pattern, delimiter):
    result = re.findall(pattern, text)
    for el in result:
        text = text.replace(el, '', 1)
    text = text.split(delimiter)
    for el in result:
        text[text.index('""')] = '\"' + el + '\"'
    return text


def export_to_file(text, res_):
    res_ = sorted(res_)
    with open(text, 'w') as file:
        for line in res_:
            file.write(line)
            file.write('\n')
    print("Готово!")