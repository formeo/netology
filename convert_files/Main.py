import os
import multiprocessing
import subprocess


def convert_file(filename):
    print('Идет конвертация файла',filename+".jpg")
    subprocess.run(["convert","Source/"+filename+".jpg", "-resize","200","Result/"+filename+"_output.jpg"])

def del_files_in_directory(dirname):
       file_list = os.listdir(dirname)
       for file in file_list:
           path = os.path.join(os.path.abspath(os.path.dirname(__file__)), dirname+'/'+file)
           os.remove(path)


def create_folder(dirname):
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    del_files_in_directory(dirname)

def get_source_files(dirname):
    files = os.listdir(dirname)
    images = filter(lambda x: x.endswith('.jpg'), files)
    files_without_ext=[]
    for  file_name in images:
        files_without_ext.append(file_name[:-4])
    return files_without_ext


def main_fuction():
    print('Вас приветствует программа конвертации файлов')
    del_files_in_directory('Result')
    create_folder('Result')
    file_list=get_source_files('Source')
    p = multiprocessing.Pool(4)
    p.map(convert_file, file_list)
    print('Все файлы переконвертированны, спасибо')



if __name__ == "__main__":
    main_fuction()