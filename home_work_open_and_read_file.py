from pprint import pprint
import os
'''
# task_1
cook_book = {}
ingredient_attribute = ['ingredient_name','quantity','measure']

with open( 'file.txt', encoding = 'utf-8') as file:

    for line in file:
        dish = line.strip()  # key dict
        count = int(file.readline().strip())

        ingredient_list = []

        for i in range(count):
            k = file.readline().strip()  # str
            s = k.split(' | ' )   # list
            ingredients = dict(zip(ingredient_attribute, s))
            ingredient_list.append(ingredients)

        file.readline().strip()

        cook_book.setdefault(dish,ingredient_list)



#print(cook_book)


# task_2


def get_shop_list_by_dishes(dishes, person_count):

    ingredients_for_dishes = {}

    for dish in dishes:
        attribute_list = ['measure', 'quantity']
        if dish in cook_book:

            for i in cook_book[dish]:
                value_list = []
                value_list.append(i['measure'])
                multiplication_quantity = int(i['quantity']) * person_count
                value_list.append(multiplication_quantity)

                result = dict(zip(attribute_list, value_list))

                if i['ingredient_name'] in ingredients_for_dishes:
                    ingredients_for_dishes[i['ingredient_name']]['quantity'] = int(ingredients_for_dishes[i['ingredient_name']]['quantity']) + int(result['quantity'])        # str

                else:
                    ingredients_for_dishes[i['ingredient_name']] = result

        else:
            print(f'{dish} такого блюда нет в меню!!!')


    pprint(ingredients_for_dishes)


get_shop_list_by_dishes(['Омлет','Утка по-пекински','Запеченный картофель','Фахитос'], 3 )

'''

# task_3

path = r"C:\Users\rudol\Desktop\home_work_open_and_read_file\work_file.txt"

def create_file(name, path):
    file = open( name , 'w')
    file.closed

def func_work_file(path):
    os.chdir(path) # переходим в директорию указанную в пути
    len_list = []
    dictionary_files = {}
    folder = os.listdir(path) # list    ['1.txt', '2.txt', '3.txt']
    print(folder)
    for file in folder:     # str
        with open(file, encoding='utf-8') as f:
            lenght = len(f.readlines())
            dictionary_files[lenght] = file
            len_list.append(lenght)

    print(dictionary_files)     # {8: '1.txt', 1: '2.txt', 9: '3.txt'}
    print(len_list)             # [8, 1, 9]

    for i in range(len(len_list) -1):   # 3-1
        if len_list[i] > len_list[i+1]:
            len_list[i+1],len_list[i] = len_list[i],len_list[i+1]

    print(len_list) # [1, 8, 9]

    create_file('total.txt', path)    # function create file txt



    temporarilly_list = []

    for key_ in len_list:
        file = dictionary_files[key_]

        f = open(file, encoding='utf-8')
        string = f.readlines()

        temporarilly_list.append(string)
        print(temporarilly_list)

        f.close()

        total_file = open('total.txt', 'a', encoding='utf-8')
        total_file.write(f'{file} \n')
        total_file.write(f'{key_} \n')
        for k in string:
            total_file.write(k)
        total_file.write('\n')
        total_file.close()



















func_work_file(r"C:\Users\rudol\Desktop\home_work_open_and_read_file\work_file.txt")