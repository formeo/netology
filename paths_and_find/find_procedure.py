import os
import re
migrations = 'Migrations'
migrations_dir = os.path.dirname(os.path.abspath(migrations))

def search_in_list(search_text,seach_list):
    r = re.compile(search_text,  flags = re.IGNORECASE)
    newlist = list(filter(r.findall, seach_list))
    return newlist

def print_list(in_list):
    for item in in_list:
        print(item)
    print('Всего файлов: ',len(in_list))

def get_file_list(dirname):
    file_list = os.listdir(dirname)
    return file_list

if __name__ == '__main__':
    find_list = []
    find_list = get_file_list(migrations_dir + '\\' + migrations)
    while True:
      search_text = input('Введите строку: ')
      find_list = search_in_list(search_text.lower(),find_list)
      print_list(find_list)