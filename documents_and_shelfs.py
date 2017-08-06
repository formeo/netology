# p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;
# l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";
# s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
# a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.
# Задача №2. Дополнительная (не обязательная)
#
# d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок;
# m – move – команда, которая спросит номер документа и целевую полку и переместит его с текущей полки на целевую;
# as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень;

documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
      ]

directories = {
        '1': ['2207 876234', '11-2'],
        '2': ['10006'],
        '3': []
      }

# функция поиска по номеру документа
def get_man_by_number():
    print('Поиск имени по номеру документа')
    doc_number=input('введите номер документа ')
    for enum in documents:
        if enum['number'] == doc_number:
            print('')
            print('Имя:',enum['name'])

# функция списока документов
def get_documents_list():
    print('Список документов:')
    for enum in documents:
        print(('"{}" "{}" "{}"').format(enum['type'], enum['number'], enum['name']))

# функция поиска полки документа
def get_shelf_number_by_doc():
    print('Поиск полки документа')
    doc_number = input('введите номер документа ')
    for enum in documents:
        if enum['number'] == doc_number:
            for enum_directories_key, enum_directories_value in directories.items():
                if doc_number in enum_directories_value:
                    print('')
                    print('полка номер:',enum_directories_key)

# функция добавления нового документа
def add_new_doc():
    print('Добавление нового документа')
    new_doc=input('введите номер документа, тип, имя владельца и номер полки через запятую ').split(',')
    documents.append({"type":new_doc[1],"number":new_doc[0],"name":new_doc[2]})
    directories[new_doc[3]].append(new_doc[0])

# функция удаления документа
def delete_doc_by_number():
    print('Удаление документа')
    doc_number = input('введите номер документа ')
    for enum in documents:
        if enum['number'] == doc_number:
           documents.remove(enum)
        for enum_directories_value in directories.values():
            if doc_number in enum_directories_value:
                enum_directories_value.remove(doc_number)

# функция перемещение документа
def move_doc_s_to_s():
    print('Перемещение документа')
    new_doc = input('введите номер документа и новую полку через запятую ').split(',')
    for enum_directories_value in directories.values():
        if new_doc[0] in enum_directories_value:
            enum_directories_value.remove(new_doc[0])
    for enum_directories_key in directories.keys():
        if new_doc[1] in enum_directories_key:
            directories[enum_directories_key].append(new_doc[0])
    print(directories)
# функция добавлени новой полки
def add_new_shelf():
    print('Добавлени новой полки')
    new_shelf = input('введите номер новый номер полки ')
    for enum_directories_key in directories.keys():
        if new_shelf == enum_directories_key:
            print('такая полка уже есть')
            return
    directories[new_shelf]=[]

# dictionary для запуска функций
functions = {
    'p': get_man_by_number,
    'l': get_documents_list,
    's': get_shelf_number_by_doc,
    'a': add_new_doc,
    'd': delete_doc_by_number,
    'm': move_doc_s_to_s,
    'as':add_new_shelf
}

# проверка правильного вводо от пользователя
def check_user_input():
    print(
        "\np - people – Показать имя человека по номеру документа, "
        "\nl – list – Показать список всех документов, "
        "\ns – shelf – Показать номер полки по номеру документа"     
        "\na – add – добавить новый документ"
        "\nd – delete  – удалить документ по номеру"
        "\nm – move  – переместить документ с полки на полку по номеру"
        "\nas – add shelf – добавить новую полку"
       )
    user_input = input('\nвведите команду: ')
    if user_input.lower().strip() in {'p','l','s','a','d','m','as'}:
        return user_input.lower().strip()


# главная функция
def main():
   while True:
     print('Вас приветствует Виртуальный секретарь. ')
     print('Команды:')
     inp=check_user_input()
     if inp:
         print('')
         functions[inp]()




main()
