import requests
import time
import json
from jsonfile import file_jason_process

# Дипломный проект
#
# Автор: Гордиенко Роман Леонидович
#
# 2017

#
# Вывести список групп в ВК в которых состоит пользователь, но не состоит никто из его друзей.


# Входные данные:
# имя пользователя или его id в ВК, для которого мы проводим исследование
# Внимание: и имя пользователя (tim_leary) и id (5030613)  - являются валидными входными данными
# Ввод можно организовать любым способом:
# из консоли
# из параметров командной строки при запуске
# из переменной

class VkProcessing:

    ACCESS_TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'

    my_groups = {}
    finish_group = {}
    write_file_class = None


    def __init__(self, user_name, user_id, write_file_class):
        self.user_id = user_id
        self.user_name = user_name
        self.write_file_class = write_file_class

    def get_friends(self):
        params = {
            'access_token': self.ACCESS_TOKEN,
            'user_id': self.user_id,
            'v': '5.68'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()['response']['items']

    def get_group_list_by_user(self, user_id):
        params = {
            'access_token': self.ACCESS_TOKEN,
            'user_id': user_id,
            'v': '5.68'
        }
        response = requests.get('https://api.vk.com/method/groups.get', params)
        try:
            return response.json()['response']['items']
        except KeyError:
            return []

    def get_main_processing(self):
        my_friend_list = self.get_friends()
        print('Start processing...')
        my_groups = set(self.get_group_list_by_user(self.user_id))
        len_friends = len(my_friend_list)
        finish_group = my_groups
        for i, item in enumerate(my_friend_list):
            print('get ', i, ' from ', len_friends, ' friends processed')
            time.sleep(0.5)
            friend_groups_set = set(self.get_group_list_by_user(item))
            finish_group = finish_group.difference(friend_groups_set)
        return finish_group

    def get_group_info(self, group_id):
        params = {
            'access_token': self.ACCESS_TOKEN,
            'group_id': group_id,
            'fields': 'members_count',
            'v': '5.68'
        }
        response = requests.get('https://api.vk.com/method/groups.getById', params)
        try:
            return {'name': response.json()['response'][0]['name'], 'gid': group_id,
                    'members_count': response.json()['response'][0]['members_count']}
        except KeyError:
            return {}

    def groups_to_json(self):
        result_list = []
        group_list = self.get_main_processing()
        len_group_list = len(group_list)
        for i, item in enumerate(group_list):
            print(i,' from ',len_group_list,' group processed')
            time.sleep(0.5)
            if self.get_group_info(item) != {}:
                result_list.append(self.get_group_info(item))
        res_file = self.write_file_class.create_result_file('groups.json')
        self.write_file_class.write_into_file(res_file,result_list)
        self.write_file_class.close_file(res_file)




write_file_class = file_jason_process.FileJsonProcess()
config_data = write_file_class.read_file('config.json')
metrika = VkProcessing(config_data['config']['user_name'], config_data['config']['user_id'], write_file_class)
metrika.groups_to_json()
