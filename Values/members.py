from Values.procedures.create.base import BaseValue


class Members:
    EIS = {'login': 'Диксон',
           'password': '123456789',
           'EIS': True,  # Заказчик с признаком ЕИС
           'price': False,  # Не может заполнять поле Без указания цены
           'classifier': '4649', }  # Способ закупки по ЕИС

    No_EIS = {'login': 'AutotestCust',
              'password': 'Automat0',
              'EIS': False,
              'price': "10 000,01", }  # Цена на создании процедуры, False - без указания цены

    suppliers = [{'login': 'AutotestSupp2',
                  'password': 'Automat0',
                  'price': BaseValue().random(3, 4, ['number']) + ',' + BaseValue().random(2, 2, ['number']), },

                 {'login': 'AutotestSupp1',
                  'password': 'Automat0',
                  'price': BaseValue().random(3, 4, ['number']) + ',' + BaseValue().random(2, 2, ['number']), }
                 ]

    ADMIN_ETP = {"login": "admin",
                 "password": "kahkahjoh1"}

    ACCOUNTANT_ETP = {"login": "accountant",
                      "password": "kahkahjoh1"}

    LOGINS = (No_EIS,)