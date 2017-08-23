import json
import  chardet
import collections
import operator

def delete_small_words(listname):
    result_list = []
    for i in listname:
        if len(i) >= 6:
            result_list.append(i)
    return result_list

def decode_file_to_json(filename):
    with open(filename, 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
        text = data.decode(result['encoding'])
        return json.loads(text)

def parse_file(filename):
    news_str = ''
    data = decode_file_to_json(filename)
    for news in data['rss']['channel']['items']:
        news_str += news['description']

    news_list = delete_small_words(news_str.split(' '))
    c = collections.Counter()
    for word in news_list:
        c[word] += 1
    sorted_news_reverse = sorted(c.items(), key=operator.itemgetter(1))[::-1]
    result_words = [sorted_news_reverse[i] for i in range(10)]
    list_words = [x[0] for x in result_words]
    return list_words

def get_all_news_from_json():
    print('Топ 10 слов в файле newsfr.json:',parse_file('newsfr.json'))
    print('Топ 10 слов в файле newsit.json:', parse_file('newsit.json'))
    print('Топ 10 слов в файле newsafr.json:', parse_file('newsafr.json'))
    print('Топ 10 слов в файле newscy.json:', parse_file('newscy.json'))

def get_all_news_from_xml():
    print('Not implemented yet')

def create_news_list():
    type_load = int(input('получить новости из 1 - json, 2 - xml '))
    if type_load == 1:
        get_all_news_from_json()
    elif type_load == 2:
        get_all_news_from_xml()


create_news_list()
