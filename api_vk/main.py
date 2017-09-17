import requests
import time
# from urllib.parse import urlencode
# AUTHORIZE_URL = 'https://oauth.vk.com/authorize'
#
# CLIENT_ID = 6184769
#
# REDIRECT_URI = ''
#
# auth_data = {
#
#     'client_id' : CLIENT_ID,
#     'display' : 'popup',
#     'response_type' : 'token',
#     'scope' : 'friends',
#     'v' : '5.68'
# }
#
# token_uri = '?'.join((AUTHORIZE_URL,urlencode(auth_data)))
# print (token_uri)

ACCESS_TOKEN='60d7feb4c33b72f610ac8d7ab9aa4b71bfaf4c67f5d1b51ef979acc2b183347483cd08d513feb111e9edd'


def get_friends(user_id):
    if user_id == None:
        params = {
            'access_token': ACCESS_TOKEN,
            'v': '5.68'
        }
    else:
        params = {
        'access_token' : ACCESS_TOKEN,
        'user_id' : user_id,
        'v' : '5.68'
        }
    response = requests.get('https://api.vk.com/method/friends.get', params)
    return response.json()['response']['items']

def print_inter_friends(friends):
    friends = list(friends)
    print('Общие друзья:')
    for item in friends:
        params = {
            'access_token': ACCESS_TOKEN,
            'user_ids': item,
            'v': '5.68'
        }
    response = requests.get('https://api.vk.com/method/users.get', params)
    for item in response.json()['response']:
        print(item['first_name']+ ' '+item['last_name'])

def get_intersection(result_set,my_friend_list):
    len_friends = len(my_friend_list)
    for i, item in enumerate(my_friend_list):
        print('get ',i,' form ',len_friends,' friends')
        time.sleep(0.5)
        frends_list = get_friends(item)
        if result_set & set(frends_list) != set():
            all_friends =  result_set & set(frends_list)
        result_set = set(all_friends)
    return result_set

def main_function():
    print('Start processing...')
    my_friend_list = get_friends(None)
    result_set = set(my_friend_list)
    print_inter_friends(get_intersection(result_set, my_friend_list))




main_function()
