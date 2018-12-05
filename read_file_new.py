def read_file(name_file, dishes, person_count):
    f = open(name_file,'r')
    cook_book = {}
    list_ingredient = []

    for line in f:
        name_dish = line.strip()
        number_ingredients = f.readline()
        cook_book[name_dish] = []
        y = 0

        while y <= (int(number_ingredients)):
            ingredient = f.readline().split('|')
            new_i = [i.strip() for i in ingredient]
            if new_i[0] == '':
                pass
            else:
                cook_book[name_dish].append({'name':new_i[0],'quantity':new_i[1], 'measure':new_i[2]})
            y += 1
    print(cook_book)
    print('__________________________________________')

    for dish in dishes:
        list_ingredient.append(cook_book[dish])
    for x in list_ingredient:
        for i in x:
            print('{}: {}{}{}, {}{}'.format(i['name'],'{',"'measure':", i['measure'], "'quantity':", int(i['quantity'])*person_count),"}")



read_file('/home/rod/Документы/Python-developer/Python/Read_write/cook_book.txt',['Омлет', 'Утка по-пекински'], 3)
