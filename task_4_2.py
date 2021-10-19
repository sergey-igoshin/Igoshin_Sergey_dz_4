"""
DZ 2. Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
и возвращающую курс этой валюты по отношению к рублю. Использовать библиотеку requests. В качестве API можно
использовать http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API в обычном
браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса str, решить поставленную задачу?
Функция должна возвращать результат числового типа, например float. Подумайте: есть ли смысл для работы с денежными
величинами использовать вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве аргумента
передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу функции не зависящей от того, в каком
регистре был передан аргумент? В качестве примера выведите курсы доллара и евро.
"""
import requests
import xmltodict
from decimal import *


def currency_rates(cur):
    resp = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').content
    data = xmltodict.parse(resp)
    for i in data['ValCurs']['Valute']:
        if i['CharCode'] == cur:
            return f'{i["CharCode"]} {i["Name"]} {Decimal(i["Value"].replace(",", "."))}'
    return


cur = input('Введите код валюты в формате USD, EUR, GBP, ... ').upper()
print(currency_rates(cur))
