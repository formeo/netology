import os
migrations = 'Migrations'
migrations_dir = os.path.dirname(os.path.abspath(migrations))

def search_in_list(search_text, search_list):
    search_text = search_text.upper()
    res_list = []
    for item in search_list:
        with open(item) as f:
            file = f.read()
            file = file.upper()
            if search_text in file:
                res_list.append(item)
    return res_list

def print_list(in_list):
    for item in in_list:
        print(item)
    print('Всего файлов: ', len(in_list))

def get_file_list(dirname):
    file_list = [os.path.join(migrations, f) for f in os.listdir(dirname) if f.endswith('.sql')]
    return file_list

if __name__ == '__main__':
    find_list = []
    find_list = get_file_list(os.path.join(migrations_dir, migrations))
    while True:
      search_text = input('Введите строку: ')
      find_list = search_in_list(search_text.lower(), find_list)
      print_list(find_list)
