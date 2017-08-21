import json
import xml.etree.ElementTree as ET

def get_all_dishes_from_json():
    dishes = {}
    with open('recepies.json') as data_file:
        data = json.load(data_file)
        recipies_list=data["recepies"]
        for recipe in recipies_list:
            name_ingridient = recipe["productName"].lower()
            count_ingridients = recipe["quant_ingridients"]
            sum_list = list()
            for recipe_ingridient in recipe["ingridients"]:
                sum_list.append(dict(ingridient_name=recipe_ingridient["ingridientName"], quantity=int(recipe_ingridient["ingridientQuant"]), measure=recipe_ingridient["ingridientUnits"]))
                dishes[name_ingridient] = sum_list
    return dishes

def get_all_dishes_from_xml():
    dishes = {}
    tree = ET.parse('recepies.xml')
    root = tree.getroot()
    recept_list = root.findall('recept')
    for recipe in recept_list:
        name_ingridient = recipe[0].text.lower()
        sum_list = list()
        for recipe_ingridient in recipe[2]:
            sum_list.append(dict(ingridient_name=recipe_ingridient.attrib["name"], quantity=int(recipe_ingridient.attrib["quant"]), measure=recipe_ingridient.attrib["units"]))
            dishes[name_ingridient] = sum_list
    return dishes

def show_current_menu(dishes_from_file):
    print('Сегодня в меню следующие блюда: ')
    for dish in dishes_from_file:
        print(dish)
    print(' ')


def get_shop_list_by_dishes(dishes, person_count,dishes_from_file):
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
    type_load = int(input('Введите способ загрузки 1 - json, 2 - xml '))
    if type_load == 1:
        dishes_from_file = get_all_dishes_from_json()
    elif type_load == 2:
        dishes_from_file = get_all_dishes_from_xml()

    show_current_menu(dishes_from_file)
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count, dishes_from_file)
    print_shop_list(shop_list)


create_shop_list()
