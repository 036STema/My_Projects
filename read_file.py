def write_new_dish(dish, ingredients):
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


cook_book = {}

f = open('/home/rod/Документы/Python-developer/Python/Read_write/cook_book.txt','r')
for line in f:
    name_dish = line.strip()
    number_ingredients = f.readline()
    cook_book[name_dish] = []
    pusto_strip(int(number_ingredients))
f.close()

print(cook_book)
