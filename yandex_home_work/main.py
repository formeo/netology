# Домашнее задание по Yandex метрике
from pprint import pprint
from urllib.parse import urlencode

import requests

APP_ID = 'f4a2975d6fa84fbda1f164c90bb93d16'
AUTHORIZE_URL = 'https://oauth.yandex.ru/authorize'

auth_data = {
    'response_type' : 'token',
    'client_id' : APP_ID
}

# print('?'.join((AUTHORIZE_URL,urlencode(auth_data))))

APP_TOKEN='AQAAAAAAQlimAASOrV5mI1QOpUgilN_kPc2jySQ'

class GetYandexMetrika:

    MANAGEMENT_URL = 'https://api-metrika.yandex.ru/management/v1/counters'
    STAT_URL = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self,token):
        self.token = token

    def get_headers(self):
         return {
             'Content-Type' : 'application/json',
             'Authorization' : 'OAuth {}'.format(self.token)
         }

    def get_counters(self):
        headers = self.get_headers()
        response = requests.get(self.MANAGEMENT_URL, headers=headers)
        return response.json()['counters']

    def get_data(self,params_in):
        headers = self.get_headers()
        params = params_in
        response = requests.get(self.STAT_URL, params, headers=headers)
        if response.json()['data'] == []:
            return 0
        else:
            return response.json()['data'][0]['metrics'][0]

    def get_visits(self,counter_id):
         params = {
             'id' : counter_id,
             'metrics' : 'ym:s:visits'
         }
         return self.get_data(params)

    def get_views(self,counter_id):
        params = {
            'id' : counter_id,
            'metrics' : 'ym:s:pageviews'
        }
        return self.get_data(params)

    def get_visitors(self,counter_id):
        params = {
        'id': counter_id,
        'metrics' : 'ym:s:users'
        }
        return self.get_data(params)

    def get_all_data(self):
        counters = self.get_counters()
        visits = 0
        views = 0
        users = 0
        for counter in counters:
            visits += self.get_visits(counter['id'])
            views += self.get_views(counter['id'])
            users += self.get_visitors(counter['id'])
        print('Всего визитов: {0}, просмотров: {1}, поситетелей: {2} '.format(visits, views, users))


metrika = GetYandexMetrika(APP_TOKEN)
metrika.get_all_data()
