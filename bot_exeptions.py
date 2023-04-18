import requests
import json
from config import *


class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(forth: str, into: str, amount: str):
        # assert type(forth) == str, 'Введите правильное значение!'
        # assert type(into) == str, 'Введите правильное значение!'
        # assert type(amount) == str, 'Введите правильное значение!'

        if forth == into:
            raise APIException(f'Невозможно перевести одинаковые валюты.'
                               f'\n/values cписок всех доступных валют.'
                               f'\n/help для помощи в написании сообщения.')

        try:
            convert_forth = values[forth]
        except KeyError:
            raise APIException(f'Невозможно конвертировать "{forth}"'
                               f'\nУбедитесь, что вы ввели команду правильно: /help, /values')

        try:
            convert_into = values[into]
        except KeyError:
            raise APIException(f'Невозможно конвертировать "{into}"'
                               f'\nУбедитесь, что вы ввели команду правильно: /help, /values')

        try:
            amount = float(amount.replace(",", "."))
        except KeyError:
            raise APIException(f'Не удалось обработать колличество "{amount}"')

        c = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={convert_forth}&tsyms={convert_into}')

        convertation = json.loads(c.content)[values[into]]

        return convertation