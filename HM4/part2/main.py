import rw_my_file
import sys


def checking_command(command):
    command = command.split(' ', 2)
    if 3 != len(command):
        print('Команда неверного формата, должно быть \"[Ключ] [символ сравнения] [Значение]\"')
        return 0
    if not command[0] in hash_dict_:
        print(f'Невалидный ключ {command[0]}')
        return 0
    if not command[1] in ['<', '==', '>']:
        print(f'Невалидный символ сравнения \'{command[1]}\', используйте \'<\', \'==\', \'>\'')
        return 0
    if '==' == command[1] and not command[2] in hash_dict_[command[0]]:
        print(f'Нет значений \'{command[2]}\' по ключу \'{command[1]}\'')
        return 0
    return command


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def start_parse():
    print(f'Я советую подходящие игры из Steam на основе фильтров. Доступны следующие параметры')
    print(list(hash_dict_.keys()))
    print('Пример использования: english == 1')
    print('Пример использования: publisher == Valve')
    print('Пример использования: platforms == linux')
    print('Пример использования: price < 4.0')
    print('Сбросить все фильтры: reset')
    print('Для формирования отчета ввести: export = \"filename\"')
    print('\nЕсли все понятно, тогда начнем!')

    result_ = set(games_.values())
    i = 0
    while 1:
        i += 1
        command = input()
        if command == 'reset':
            result_ = set(games_.values())
            print(f"Найдено результатов: {len(result_)}")
            continue
        if command.split(' ')[0] == 'export':
            rw_my_file.export_to_file(f'{command.split(" ")[2]}.csv', result_)
            break
        command = checking_command(command)
        if not command:
            continue
        tmp_ = set()
        match command[1]:
            case '==':
                for item in hash_dict_[command[0]][command[2]]:
                    tmp_.add(games_[item])
            case '<':
                for key in hash_dict_[command[0]].keys():
                    flot_key = key
                    if is_number(flot_key):
                        flot_key = float(flot_key)
                        command[2] = float(command[2])
                    if flot_key < command[2]:
                        for item in hash_dict_[command[0]][key]:
                            tmp_.add(games_[item])
            case '>':
                for key in hash_dict_[command[0]].keys():
                    flot_key = key
                    if is_number(flot_key):
                        flot_key = float(flot_key)
                        command[2] = float(command[2])
                    if flot_key > command[2]:
                        for item in hash_dict_[command[0]][key]:
                            tmp_.add(games_[item])
        result_ = result_.intersection(tmp_)
        print(f"Найдено результатов: {len(result_)}")


if __name__ == "__main__":
    games_, hash_dict_ = rw_my_file.read_file(sys.argv[1])
    start_parse()
else:
    games_, hash_dict_ = rw_my_file.read_file('practice-2-main/test')
    start_parse()