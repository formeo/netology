# cook_book = {
#     'яйчница': [
#         {'ingridient_name': 'яйца', 'quantity': 2, 'measure': 'шт.'},
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'}
#     ],
#     'стейк': [
#         {'ingridient_name': 'говядина', 'quantity': 300, 'measure': 'гр.'},
#         {'ingridient_name': 'специи', 'quantity': 5, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 10, 'measure': 'мл.'}
#     ],
#     'салат': [
#         {'ingridient_name': 'помидоры', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'огурцы', 'quantity': 100, 'measure': 'гр.'},
#         {'ingridient_name': 'масло', 'quantity': 100, 'measure': 'мл.'},
#         {'ingridient_name': 'лук', 'quantity': 1, 'measure': 'шт.'}
#     ]
# }

def get_all_dishes():
    dishes = {}
    with open('recipies.txt', 'r') as dish_file:
        for line in dish_file:
            name_ingridient = line.strip().lower()
            count_ingridients = dish_file.readline()
            i = 0
            sum_list = list()
            for i in range(int(count_ingridients)):
                ingridient = dish_file.readline().split('|')
                ingridient = [line.strip() for line in ingridient]
                sum_list.append( dict(ingridient_name = ingridient[0], quantity = int(ingridient[1]), measure = ingridient[2]))
                dishes[name_ingridient] = sum_list
            dish_file.readline()
    return dishes

def show_current_menu(dishes_from_file):
    print('Сегодня в меню следующие блюда: ')
    for dish_name in dishes_from_file:
        print(dish_name)
    print(' ')


def get_shop_list_by_dishes(dishes, person_count, dishes_from_file):
    shop_list = {}
    for dish in dishes:
        for ingridient in dishes_from_file[dish]:
            new_shop_list_item = dict(ingridient)

            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] +=  new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))


def create_shop_list():
    dishes_from_file = get_all_dishes()
    show_current_menu(dishes_from_file)
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, dishes_from_file)
    print_shop_list(shop_list)


create_shop_list()
