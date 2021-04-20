from pprint import pprint

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