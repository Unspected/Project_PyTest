import datetime
from mimesis import Person
from mimesis.enums import Gender
from mimesis import Address
from mimesis.schema import Field
from mimesis import builtins as b
from mimesis import Business
from mimesis import locales
from mimesis import Code
import random


class BaseRegisterValue:
    def __init__(self, role, type_company):
        self.new_user_RF = self.new_data_contragent(role, type_company)
        self.new_user_SNG = self.new_data_contragent_SNG(role, type_company)
        self.new_user_foreign = self.new_data_contragent_Foreign(role, type_company)

    def new_data_contragent(self, role, type_company):
        bik = ["044525225",
               "044525187",
               "044525593"]

        extra = (
            b.RussiaSpecProvider,
        )
        data_company = Field(locales.RU, providers=extra)

        new_user = {
            "login": Person(locales.RU).username(),
            "password": "123456789",
            "user_mail": Person(locales.RU).email(),
            "first_name_user": Person(locales.RU).name(Gender.MALE),
            "last_name_user": Person(locales.RU).last_name(Gender.MALE),
            "job_user": Person('ru').occupation(),
            "user_phone": Person('ru').telephone('8##########'),
            "resident": 1,
            "role": role,
            "type_company": type_company,
            "name_company": Business(locales.RU).company_type() + ' \"' + Business(locales.RU).company() + '\"',
            "name_IP": "Индивидуальный предприниматель " + Person('ru').full_name(Gender.MALE),
            "inn": data_company('inn'),
            "kpp": data_company('kpp'),
            "ogrn": data_company('ogrn'),
            "general_email": Person(locales.EN).email(),
            "general_phone": Person('ru').telephone('7##########'),
            "index": Address('ru').postal_code(),
            "region": "Москва",
            "city": Address('ru').city(),
            "street": Address('ru').street_suffix() + " " + Address('ru').street_name(),
            "house": Address('ru').street_number(),
            "last_name": Person(locales.RU).last_name(Gender.FEMALE),
            "first_name": Person(locales.RU).name(Gender.FEMALE),
            "middle_name": Person(locales.RU).name(Gender.FEMALE),
            "job": Person('ru').occupation(),
            "bank_account": "30101810400000000225",
            "bik": bik[random.randint(0, 2)]}

        return new_user

    def new_data_contragent_SNG(self, role, type_company):
        extra = (
            b.RussiaSpecProvider,
        )
        data_company = Field(locales.RU, providers=extra)

        new_user_SNG = {
            "login": Person(locales.RU).username(),
            "password": "123456789",
            "user_mail": Person(locales.RU).email(),
            "first_name_user": Person(locales.RU).name(Gender.MALE),
            "last_name_user": Person(locales.RU).last_name(Gender.MALE),
            "job_user": Person('ru').occupation(),
            "user_phone": Person('ru').telephone('8##########'),
            "resident": 2,
            "role": role,
            "type_company": type_company,
            "name_company": Business(locales.RU).company_type() + ' \"' + Business(locales.RU).company() + '\"',
            "register_number": data_company('kpp'),
            "tin": data_company('snils'),
            "inn": data_company('inn'),
            "general_email": Person(locales.EN).email(),
            "general_phone": Person('ru').telephone('7##########'),
            "country": "Беларусь",
            "index": Address('ru').postal_code(),
            "region": "Минск",
            "city": Address('ru').city(),
            "street": Address('ru').street_suffix() + " " + Address('ru').street_name(),
            "house": Address('ru').street_number(),
            "last_name": Person(locales.RU).last_name(Gender.FEMALE),
            "first_name": Person(locales.RU).name(Gender.FEMALE),
            "middle_name": Person(locales.RU).name(Gender.FEMALE),
            "job": Person('ru').occupation(),
            "bank_account": Code().imei(),
            "iban": Code().ean(),
            "bank_name": "Sberbank_Belarus",
            "bank_swift": "SABRRUMM"
        }

        return new_user_SNG

    def new_data_contragent_Foreign(self, role, type_company):
        extra = (
            b.RussiaSpecProvider,
        )
        data_company = Field(locales.RU, providers=extra)

        new_user = {
            "login": Person(locales.EN).username(),
            "password": "123456789",
            "user_mail": Person(locales.EN).email(),
            "first_name_user": Person(locales.EN).name(Gender.MALE),
            "last_name_user": Person(locales.EN).last_name(Gender.MALE),
            "job_user": Person('en').occupation(),
            "user_phone": Person('en').telephone('8##########'),
            "resident": 3,
            "role": role,
            "type_company": type_company,
            "name_company": Business(locales.EN).company_type() + ' \"' + Business(locales.EN).company() + '\"',
            "register_number": data_company('kpp'),
            "tin": data_company('snils'),
            "inn": data_company('inn'),
            "general_email": Person(locales.EN).email(),
            "general_phone": Person('en').telephone('7##########'),
            "country": "Канада",
            "index": Address('en').postal_code(),
            "region": "Vancouver",
            "city": Address('en').city(),
            "street": Address('en').street_suffix() + " " + Address('en').street_name(),
            "house": Address('en').street_number(),
            "last_name": Person(locales.EN).last_name(Gender.FEMALE),
            "first_name": Person(locales.EN).name(Gender.FEMALE),
            "middle_name": Person(locales.EN).name(Gender.FEMALE),
            "job": Person('en').occupation(),
            "bank_account": Code().imei(),
            "iban": Code().ean(),
            "bank_name": "BANK OF CANADA",
            "bank_swift": "CAAANDAY"
        }

        return new_user
