import random
import string


class BaseValue:

    def __init__(self):
        self.set_procedure_name()
        self.procedure_price = 10000

    registry_number = None
    procedure_name = None
    STRING_RUS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    UP_STRING_RUS = STRING_RUS.upper()

    string_symbol = {'number': string.digits,
                     'string_eng': string.ascii_lowercase,
                     'up_string_eng': string.ascii_uppercase,
                     'eng_letters': string.ascii_letters,
                     'string_rus': STRING_RUS,
                     'up_string_rus': UP_STRING_RUS,
                     'symbol': string.punctuation,
                     'all': (string.digits
                             + string.ascii_letters
                             + STRING_RUS
                             + UP_STRING_RUS
                             + string.punctuation
                             + ' '),
                     'email': (string.digits
                               + string.ascii_letters
                               + "_-"),
                     'procedure_name': string.hexdigits}

    def set_procedure_name(self):
        self.procedure_name = "[TEST]_" + self.random(13, 13, ['procedure_name'])

    def any_values(self):
        pass

    def random(self, min=3, max=15, symbol=('all',)):
        """
        Генератор случайной строки\n
        :param min: Минимальное число символов
        :param max: Максимальное число символов
        :param symbol: Один из словарей:
                     'number', 'string_eng', 'up_string_eng', 'eng_letters',
                     'string_rus', 'up_string_rus', 'symbol', 'all', 'email',
                     'procedure_name'}
        :return: Возвращает случайную строку со случайной длинной
         из указанного словаря symbol, длинной от min до max.
        """
        rand = random.randint(min, max)
        string = ''
        for x in symbol:
            string += self.string_symbol[x]
        return (''.join([random.choice(string) for x in range(rand)]))
