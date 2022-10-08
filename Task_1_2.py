import os

recipes_path = os.path.join(os.getcwd(), 'recipes.txt')

cook_book = {}

with open(recipes_path, 'rt', encoding='utf8') as file:
    for i in file:
        dish_name = i.strip()
        ingredients_count = file.readline()
        ingredients_list = []
        for ing in range(int(ingredients_count)):
            ingredient = file.readline()
            ingredient_name, quantity, measure = ingredient.strip().split(' | ')
            ingredients_list.append({'ingredient_name': ingredient_name,
                                      'quantity': int(quantity),
                                      'measure': measure})
        blank_line = file.readline()
        cook_book[dish_name] = ingredients_list
print(cook_book)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] not in shop_list:
                    shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'],
                                                          'quantity': ingr['quantity'] * person_count}
                else:
                    for x in shop_list[ingr['ingredient_name']]:
                        shop_list[ingr['ingredient_name']]['quantity'] += ingr['quantity']
        else:
            print(f'{dish} в кулинарной книге нет!')
            return
    print(shop_list)


get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)