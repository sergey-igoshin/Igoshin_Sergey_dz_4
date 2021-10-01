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
