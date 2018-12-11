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
print(file_sql[1])


while len(file_sql) > 1:
    list_file = []
    file_name = input('Введите строку: ')
    for file in file_sql:
        with  open('/home/rod/Документы/Python-developer/Python/{}/{}'.format(migrations,file), 'r') as file_contents:
            file_contents = file_contents.read()
            if file_name in file_contents:
                print(file_name, 'есть в файле ', file)
                list_file.append(file)
    file_sql = list_file
    list_file =[]
    print('Всего', len(file_sql))
else:
    print(file_sql)


