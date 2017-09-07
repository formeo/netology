import json
import chardet
import collections
import operator
import xml.etree.ElementTree as ET
import codecs


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


def print_list(in_list):
    for item in in_list:
        print(item)


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


def detect_xml_coding(filename):
    result = {}
    with open(filename, 'rb') as file:
        data = file.read()
        result = chardet.detect(data)
    return result


def parse_file_xml(filename):
    news_str = ''
    xmlp = ET.XMLParser(encoding=detect_xml_coding(filename)['encoding'])
    tree = ET.parse(filename, parser=xmlp)
    root = tree.getroot()
    news_list = root.findall('channel')
    for news in news_list[0].findall('item'):
        x = news.findall('description')
        for item in x:
            news_str += item.text
    news_list = delete_small_words(news_str.split(' '))
    c = collections.Counter()
    for word in news_list:
        c[word] += 1
    sorted_news_reverse = sorted(c.items(), key=operator.itemgetter(1))[::-1]
    result_words = [sorted_news_reverse[i] for i in range(10)]
    list_words = [x[0] for x in result_words]
    return list_words


def get_all_news_from_json():
    print('Топ 10 слов в файле newsfr.json:')
    print_list(parse_file('newsfr.json'))
    print('Топ 10 слов в файле newsit.json:')
    print_list(parse_file('newsit.json'))
    print('Топ 10 слов в файле newsafr.json:')
    print_list(parse_file('newsafr.json'))
    print('Топ 10 слов в файле newscy.json:')
    print_list(parse_file('newscy.json'))


def get_all_news_from_xml():
    print('Топ 10 слов в файле newsfr.xml:')
    print_list(parse_file_xml('newsfr.xml'))
    print('Топ 10 слов в файле newsit.xml:')
    print_list(parse_file_xml('newsit.xml'))
    print('Топ 10 слов в файле newsafr.xml:')
    print_list(parse_file_xml('newsafr.xml'))
    print('Топ 10 слов в файле newscy.xml:')
    print_list(parse_file_xml('newscy.xml'))


def create_news_list():
    type_load = int(input('получить новости из 1 - json, 2 - xml '))
    if type_load == 1:
        get_all_news_from_json()
    elif type_load == 2:
        get_all_news_from_xml()


create_news_list()
