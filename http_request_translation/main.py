import requests
import os
import shutil

URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
KEY = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
OUT_DIR = 'translated'

def translate_it(path_to_file_in, path_to_file_result, lang_from, lang_to = 'ru'):
    lang_from = lang_from.lower()
    language = lang_from + '-' + lang_to
    with open(path_to_file_result, 'tw', encoding = 'utf-8') as f_out:
        with open(path_to_file_in) as f_in:
            for line in f_in:
                params = {
                    'key': KEY,
                    'lang': language,
                    'text': line,
                }
                response = requests.get(URL, params=params).json()
                f_out.writelines(' '.join(response.get('text', [])))


def get_file_list():
    file_list = [f for f in os.listdir() if f.endswith('.txt')]
    return file_list

def create_out_dir(directory='translated'):
    if os.path.exists(directory):
       shutil.rmtree(directory)
    os.makedirs(directory)

def main_function():
    create_out_dir(OUT_DIR)
    files = get_file_list()
    print('Start translation')
    for item in files:
        with open(item) as f:
            file_out = os.path.join(OUT_DIR, item[:-4]+'-RU.txt')
            if os.path.exists(file_out):
                os.remove(file_out)
            translate_it(item, file_out, item[:-4], 'ru')
    print('Translated complete')

main_function()