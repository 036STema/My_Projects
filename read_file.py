def read_file(name_file):
    f = open(name_file,'r')
    cook_book = {}


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
    return cook_book

def get_shop_list_by_dishes(dishes, person_count, pith):
    new_cook_book = read_file(pith)
    list_ingredient = []

    for dish in dishes:
        list_ingredient.append(new_cook_book[dish])
    for x in list_ingredient:
        for i in x:
            print('{}: {}{}{}, {}{}'.format(i['name'],'{',"'measure':", i['measure'], "'quantity':", int(i['quantity'])*person_count),"}")



#read_file('/home/rod/Документы/Python-developer/Python/Read_write/cook_book.txt')
get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3, '/home/rod/Документы/Python-developer/Python/Read_write/cook_book.txt')

