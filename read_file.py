 write_new_dish(dish, ingredients):
    f = open('/home/rod/Документы/Python-developer/Python/Read_write/cook_book1.txt','a')
    f.write('{} \n{}\n'.format(dish, ingredients))
    x=1
    while x <= ingredients:
        name_ingredient = input('Ингредиент - ')
        quantity = input('Колличество - ')
        measure = input('Мера - ')
        f.write('{} | {} | {}\n'.format(name_ingredient ,quantity, measure))
        x +=1
    f.write('\n')
    f.close()

def cook_book_output():
    f = open('/home/rod/Документы/Python-developer/Python/Read_write/cook_book1.txt','r')
    print(f.read())

def pusto_strip(x):
    y = 0
    while y <= x:
        ingredient = f.readline().split('|')
        new_i = [i.strip() for i in ingredient]
        if new_i[0] == '':
            pass
        else:
            cook_book[name_dish].append({'name':new_i[0],'quantity':new_i[1], 'measure':new_i[2]})
        y += 1

def get_shop_list_by_dishes(dishes, person_count):
    l = []
    for dish in dishes:
        l.append(cook_book[dish])
    for x in l:
        for i in x:
            print('{}: {}{}{}, {}{}'.format(i['name'],'{',"'measure':", i['measure'], "'quantity':", int(i['quantity'])*person_count),"}")

cook_book = {}

f = open('/home/rod/Документы/Python-developer/Python/Read_write/cook_book.txt','r')
for line in f:
    name_dish = line.strip()
    number_ingredients = f.readline()
    cook_book[name_dish] = []
    pusto_strip(int(number_ingredients))
f.close()

get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 3)
print('___________________________________')
print(cook_book)


