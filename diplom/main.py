import requests
import time

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



ACCESS_TOKEN='5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'

class VkProcessing:

    ACCESS_TOKEN = '5dfd6b0dee902310df772082421968f4c06443abecbc082a8440cb18910a56daca73ac8d04b25154a1128'

    my_groups = {}
    finish_group = {}

    def __init__(self,user_name,user_id):
        self.user_id = user_id
        self.user_name = user_name

    def get_friends(self):
        params = {
            'access_token': ACCESS_TOKEN,
            'user_id': self.user_id,
            'v': '5.68'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        return response.json()['response']['items']

    def get_group_list_by_user(self,user_id):
        # print(user_id)
        params = {
            'access_token': ACCESS_TOKEN,
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
        # print(my_friend_list)
        print('Start processing...')
        my_groups = set(self.get_group_list_by_user(self.user_id))
        # print(my_groups)
        len_friends = len(my_friend_list)
        finish_group = my_groups
        for i, item in enumerate(my_friend_list):
            print('get ', i, ' from ', len_friends, ' friends processed')
            time.sleep(0.5)
            friend_groups_set = set(self.get_group_list_by_user(item))
            # print(friend_groups_set)
            finish_group = finish_group.difference(friend_groups_set)
        return finish_group


# def get_friends(user_id):
#     if user_id == None:
#         params = {
#             'access_token': ACCESS_TOKEN,
#             'v': '5.68'
#         }
#     else:
#         params = {
#         'access_token' : ACCESS_TOKEN,
#         'user_id' : user_id,
#         'v' : '5.68'
#         }
#     response = requests.get('https://api.vk.com/method/friends.get', params)
#     return response.json()['response']['items']
#
# def print_inter_friends(friends):
#     friends = list(friends)
#     print('Общие друзья:')
#     for item in friends:
#         params = {
#             'access_token': ACCESS_TOKEN,
#             'user_ids': item,
#             'v': '5.68'
#         }
#     response = requests.get('https://api.vk.com/method/users.get', params)
#     for item in response.json()['response']:
#         print(item['first_name']+ ' '+item['last_name'])
#
# def get_intersection(result_set,my_friend_list):
#     len_friends = len(my_friend_list)
#     for i, item in enumerate(my_friend_list):
#         print('get ',i,' form ',len_friends,' friends')
#         time.sleep(0.5)
#         frends_list = get_friends(item)
#         if result_set & set(frends_list) != set():
#             all_friends =  result_set & set(frends_list)
#         result_set = set(all_friends)
#     return result_set
#
# def main_function():
#     print('Start processing...')
#     my_friend_list = get_friends(None)
#     result_set = set(my_friend_list)
#     print_inter_friends(get_intersection(result_set, my_friend_list))




# main_function()

metrika = VkProcessing('tim_leary',5030613)
print(metrika.get_main_processing())