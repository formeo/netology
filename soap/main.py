from suds.client import Client
TEMP_URL = 'http://www.webservicex.net/ConvertTemperature.asmx?WSDL'
CURRENCY_URL = 'http://www.webservicex.net/CurrencyConvertor.asmx?WSDL'
TRAVEL_URL = 'http://www.webservicex.net/length.asmx?WSDL'

def read_temp_file():
    result_list = []
    with open('temps.txt', 'r') as temp_file:
        result_list = [line.strip().replace(' F', '') for line in temp_file]
    return list(map(int, result_list))

def read_currency_file():
    result_list = []
    with open('currencies.txt', 'r') as temp_file:
        result_list = [line.strip() for line in temp_file]
    return result_list

def read_travel_file():
    result_list = []
    with open('travel.txt', 'r') as temp_file:
        result_list = [line.strip() for line in temp_file]
    return result_list

def convert(temperature):
    client = Client(TEMP_URL)
    result = client.service.ConvertTemp(temperature, 'degreeFahrenheit', 'degreeCelsius')
    return result

def convert_currency(from_currency):
    client = Client(CURRENCY_URL)
    result = client.service.ConversionRate(from_currency, 'RUB')
    return result

def convert_travel(distance):
    client = Client(TRAVEL_URL)
    result = client.service.ChangeLengthUnit(distance, 'Miles','Kilometers')
    return result

def sum_trip_in_rub():
    all_sum = 0
    currency_list = read_currency_file()
    for item in currency_list:
        item_list = item.split(' ')
        all_sum += convert_currency(item_list[2]) * item_list[1]
    print(all_sum)

def avg_temperature():
    temp_list = read_temp_file()
    res_list = [convert(line) for line in temp_list]
    print(round(sum(res_list) / len(res_list), 1))

def result_distance():
    all_sum = 0
    distance_list = read_travel_file()
    for item in distance_list:
        item_list = item.split(' ')
        all_sum += convert_travel(item_list[1].replace(',', ''))
    print(round(all_sum, 2))


def main_function():
    print('Средняя температура в градусах цельсия: ')
    avg_temperature()
    print('Стоимость путешествия в рублях: ')
    sum_trip_in_rub()
    print('Суммарное расстояние пути в километрах: ')
    result_distance()


main_function()