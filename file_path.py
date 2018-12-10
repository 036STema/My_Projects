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

list_file = []

while len(file_sql) != 1:
    file_name = input('Введите, что вы ищите: ')
    if len(file_sql) == 0:
        print("Такого файла нет")
    else:
        for file in file_sql:
            with  open('/home/rod/Документы/Python-developer/Python/{}/{}'.format(migrations,file), 'r') as file_contents:
                file_contents = file_contents.read()
                if file_name in file_contents:
                    pass
                else:
                    file_sql.remove(file)
    print('Всего найдено файлов - {}'.format(len(file_sql)))
else:
    print(file_sql)


if __name__ == '__main__':
    # ваша логика
    pass



import os
os.system('/usr/bin/firefox')
