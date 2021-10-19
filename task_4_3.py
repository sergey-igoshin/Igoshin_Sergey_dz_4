"""
DZ 3. *(вместо 2) Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату, которая передаётся
в ответе сервера. Дата должна быть в виде объекта date. Подумайте, как извлечь дату из ответа, какой тип данных лучше
использовать в ответе функции?
"""

import requests
import xmltodict
from decimal import *
from datetime import datetime


def currency_rates(cur):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    data = xmltodict.parse(resp)
    for i in data['ValCurs']['Valute']:
        if i['CharCode'] == cur:
            time = data['ValCurs']['@Date'].split('.')
            day, month, year = map(int, time)
            return f'{datetime(day=day, month=month, year=year)}\n' \
                   f'{i["CharCode"]} {i["Name"]} {Decimal(i["Value"].replace(",", "."))}'
    return


cur = input('Введите код валюты в формате USD, EUR, GBP, ... ').upper()
print(currency_rates(cur))
