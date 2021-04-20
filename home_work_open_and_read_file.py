from pprint import pprint
'''
Задача №1
Должен получится следующий словарь

cook_book = {
  'Омлет': [
    {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
    {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
    {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
    ],
  'Утка по-пекински': [
    {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
    {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
    {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
    {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
    ],
  'Запеченный картофель': [
    {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
    {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
    {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
    ]
  }
'''

dish_dict = {}
#ingredient_list = []
ingredient_atribute = ['ingredient_name','quantity','measure']

with open( 'file.txt', encoding = 'utf-8') as file:

    for line in file:
        dish = line.strip()  # key dict
        count = int(file.readline().strip())

        ingredient_list = []


        for i in range(count):
            k = file.readline().strip()  # str
            s = k.split('|')   # list

            ingredients = dict(zip(ingredient_atribute, s))
            ingredient_list.append(ingredients)

        file.readline().strip()

        dish_dict.setdefault(dish,ingredient_list)



print(dish_dict)




