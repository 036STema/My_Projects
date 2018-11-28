# Задание
# мне нужно отыскать файл среди десятков других
# я знаю некоторые части этого файла (на память или из другого источника)
# я ищу только среди .sql файлов
# 1. программа ожидает строку, которую будет искать (input())
# после того, как строка введена, программа ищет её во всех файлах
# выводит список найденных файлов построчно
# выводит количество найденных файлов
# 2. снова ожидает ввод
# поиск происходит только среди найденных на этапе 1
# 3. снова ожидает ввод
# ...
# Выход из программы программировать не нужно.
# Достаточно принудительно остановить, для этого можете нажать Ctrl + C

# Пример на настоящих данных

# python3 find_procedure.py
# Введите строку: INSERT
# ... большой список файлов ...
# Всего: 301
# Введите строку: APPLICATION_SETUP
# ... большой список файлов ...
# Всего: 26
# Введите строку: A400M
# ... большой список файлов ...
# Всего: 17
# Введите строку: 0.0
# Migrations/000_PSE_Application_setup.sql
# Migrations/100_1-32_PSE_Application_setup.sql
# Всего: 2
# Введите строку: 2.0
# Migrations/000_PSE_Application_setup.sql
# Всего: 1

# не забываем организовывать собственный код в функции

import os

migrations = 'Migrations'
current_dir = os.path.dirname(os.path.abspath(migrations))
os.path.join(current_dir, migrations)
#file_list = os.listdir(path="/home/rod/Документы/Python-developer/Python/Migrations")
file_list = (os.listdir(os.path.join("/home/rod/Документы/Python-developer/Python/", migrations)))


file_sql = []
for file in file_list:
    if '.sql' in file:
        file_sql.append(file)

print('Всего найдено файлов - {}'.format(len(file_sql)))

list_find = []
def find_file(name_file):
    for name_file in file_sql:
        if 'user_g' in name_file:
            list_find.append(name_file)

    print(list_find)
    return(list_find)
            #print('Всего найдено файлов - {}'.format(len(name_file)))

name_file = input('Какой файл вы ищите? ')
find_file(name_file)


if __name__ == '__main__':
    # ваша логика
pass


import os
os.system('/usr/bin/firefox')
