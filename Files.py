# Открыть файл рецептов менеджером контекста
# Из первой строки брать название блюда
# Из второй - количество ингридиентов и строк для прочтения
# На пустрой строке завершать итерацию
# Из собранного делать словарь формата
# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }


def reader():
    with open('recepies.txt', encoding='utf8') as file:
        cook_book = {}
        while True:
            dish_name = file.readline().strip()
            ingredients_amount = int(file.readline().strip())
            complete_set = []
            for lines in range(ingredients_amount):
                complete_set_list = [file.readline().strip().split(' | ')]
                temp_dict = {'ingredient name': complete_set_list[0][0], 'quantity': complete_set_list[0][1], 'measure'
                             : complete_set_list[0][2]}
                complete_set.append(temp_dict)
            dish_recepy = {dish_name: complete_set}
            cook_book.update(dish_recepy)
            extra_line = file.readline()
            if not extra_line:
                break
    selector(cook_book)


def selector(cook_book):
    print('Доступны рецепты блюд:')
    available_dishes = {}
    selected_full =[]
    for index, items in enumerate(cook_book.keys()):
        print(f'{index + 1}. {items}')
        dishes = {index + 1: items}
        available_dishes.update(dishes)
    person = input('\nСколько гостей?\n>')
    selected = input('Что будем готовить?\nВведите индекс блюд через запятую:\n>').strip().split(',')
    print('Готовим:')
    for selected_dishes in selected:
        selected_full.append(available_dishes.get(int(selected_dishes)))
        print(available_dishes.get(int(selected_dishes)))
    shopping(selected_full, cook_book, person)


def shopping(dishes, cook_book, person):
    cart_temp = {}
    for items in dishes:
        for ingredients in cook_book.get(items):
            item_temp = {
                ingredients.get('ingredient name'):
                        {'measure': ingredients.get('measure'),
                         'quantity': ingredients.get('quantity')}
            }
            if ingredients.get('ingredient name') in cart_temp.keys():
                new_amount = str(int(ingredients.get('quantity')) +
                                 int(cart_temp.get(ingredients.get('ingredient name')).get('quantity')))
                item_temp = {
                    ingredients.get('ingredient name'):
                        {'measure': ingredients.get('measure'),
                         'quantity': new_amount}}
                cart_temp.update(item_temp)
            else:
                cart_temp.update(item_temp)
    result(cart_temp, person)


def result(cart_temp, person):
    print('\nНужно купить:')
    for food in cart_temp:
        print(food, int(cart_temp.get(food).get('quantity')) * int(person), cart_temp.get(food).get('measure'))


def main():
    reader()


main()
