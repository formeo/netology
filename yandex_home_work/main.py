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

    management_url = 'https://api-metrika.yandex.ru/management/v1/counters'
    stat_url = 'https://api-metrika.yandex.ru/stat/v1/data'

    def __init__(self,token):
        self.token = token

    def getHeaders(self):
         return {
             'Content-Type' : 'application/json',
             'Authorization' : 'OAuth {}'.format(self.token)
         }

    def GetCounters(self):
        headers = self.getHeaders()
        response = requests.get(self.management_url, headers=headers)
        return response.json()['counters']

    def GetData(self,params_in):
        headers = self.getHeaders()
        params = params_in
        response = requests.get(self.stat_url, params, headers=headers)
        if response.json()['data'] == []:
            return 0
        else:
            return response.json()['data'][0]['metrics'][0]


    def GetVisits(self,counter_id):
         params = {
             'id' : counter_id,
             'metrics' : 'ym:s:visits'
         }
         return self.GetData(params)

    def GetVievs(self,counter_id):
        params = {
            'id' : counter_id,
            'metrics' : 'ym:s:pageviews'
        }
        return self.GetData(params)

    def GetVisitors(self,counter_id):
        params = {
        'id': counter_id,
        'metrics' : 'ym:s:users'
        }
        return self.GetData(params)

    def GetAllData(self):
        counters = self.GetCounters()
        visits = 0
        views = 0
        users = 0
        for counter in counters:
            visits += self.GetVisits(counter['id'])
            views += self.GetVievs(counter['id'])
            users += self.GetVisitors(counter['id'])
        print('Всего визитов: {0}, просмотров: {1}, поситетелей: {2} '.format(visits, views, users))


metrika = GetYandexMetrika(APP_TOKEN)
metrika.GetAllData()
