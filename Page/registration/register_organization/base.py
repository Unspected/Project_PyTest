import allure
import datetime
import time
import random
from Page.base import BaseProcedures
from Page.helper import Helper
from Page.registration.base_registration import BaseRegistration


class BaseOrganizationDetails(BaseRegistration):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_organizator_info(self, value):
        with allure.step("Заполнение данных об организаторе"):
            self.select_type_company(value["type_company"])
            self.fill_legal_form()
            self.fill_name_organization(value)
            self.fill_register_date()
            self.fill_data_organization(value["inn"], value["kpp"], value["ogrn"])
            self.fill_okpo()
            self.fill_contact_organization(value["general_email"], value["general_phone"])
            self.fill_legal_adress(value["index"], value["region"], value["city"], value["street"], value["house"])
            self.information_about_head(value["last_name"], value["first_name"], value["middle_name"], value["job"])
            self.service_products_offered()
            self.bank_details(value["bank_account"], value["bik"])
            self.accept_and_register()
            self.wait_signature_text()
            self.confirm_button()

    @property
    def type_of_company(self):
        with allure.step("Тип компании"):
            return self.driver.find_element_by_xpath(
                "//div[@class='x-form-field-wrap x-form-field-trigger-wrap']//input[@class='x-form-text x-form-field x-trigger-noedit']")

    @Helper.wait_for_ajax()
    def select_type_company(self, type):
        """
        :param type: int по типу в массиве
        :return:
        """
        company = {
            1: "Юридическое лицо (РФ)",
            2: "Физическое лицо (РФ)",
            3: "Индивидуальный предприниматель (РФ)"
        }
        with allure.step(f"Выбран тип компании {company[type]}"):
            self.type_of_company.click()
            self.driver.find_element_by_xpath(f"//div[@class='x-combo-list-inner']/div[.='{company[type]}']").click()
            self.type_company = type

    @property
    def name_organization(self):
        with allure.step("Полное Наименование организации (Ф.И.О для ЮР лиц)"):
            self.driver.find_element_by_name("full_name").clear()
            return self.driver.find_element_by_name("full_name")

    @property
    def short_name_organization(self):
        with allure.step("Краткое наименование"):
            self.driver.find_element_by_xpath("//input[@name='short_name']").clear()
            return self.driver.find_element_by_xpath("//input[@name='short_name']")

    @property
    def registration_date(self):
        with allure.step("Дата постановки на учет в налоговом органе (Только Для Поставщика)"):
            self.driver.find_element_by_name("registration_date").clear()
            return self.driver.find_element_by_name("registration_date")

    @Helper.wait_for_ajax()
    def fill_legal_form(self):
        """Организационно правовая форма"""
        pass

    @property
    def inn(self):
        with allure.step("ИНН:"):
            self.driver.find_element_by_name("inn").clear()
            return self.driver.find_element_by_name("inn")

    @property
    def kpp(self):
        with allure.step("КПП:"):
            self.driver.find_element_by_name("kpp").clear()
            return self.driver.find_element_by_name("kpp")

    @property
    def ogrn(self):
        with allure.step("ОГРН:"):
            self.driver.find_element_by_name("ogrn").clear()
            return self.driver.find_element_by_name("ogrn")

    @property
    def okpo(self):
        with allure.step("ОКПО"):
            self.driver.find_element_by_name("okpo").clear()
            return self.driver.find_element_by_name("okpo")

    @property
    def general_email(self):
        with allure.step("Адресс Электронной почты (Общий)"):
            self.driver.find_element_by_name("email").clear()
            return self.driver.find_element_by_name("email")

    @property
    def general_phone_country_code(self):
        with allure.step("Телефон организации Код страны"):
            self.driver.find_element_by_name("phone[cntr_code]").clear()
            return self.driver.find_element_by_name("phone[cntr_code]")

    @property
    def general_phone_city_code(self):
        with allure.step("Телефон организации Код города"):
            self.driver.find_element_by_name("phone[city_code]").clear()
            return self.driver.find_element_by_name("phone[city_code]")

    @property
    def general_phone_number(self):
        with allure.step("Телефон организации Номер телефона"):
            self.driver.find_element_by_name("phone[number]").clear()
            return self.driver.find_element_by_name("phone[number]")

    @property
    def postcode(self):
        with allure.step("Почтовый индекс"):
            self.driver.find_element_by_name("legal[index]").clear()
            return self.driver.find_element_by_name("legal[index]")

    @property
    def region(self):
        with allure.step("Регион/Область"):
            self.driver.find_element_by_name("legal[region]").clear()
            return self.driver.find_element_by_name("legal[region]")

    @property
    def city(self):
        with allure.step("Город"):
            self.driver.find_element_by_name("legal[city]").clear()
            return self.driver.find_element_by_name("legal[city]")

    @property
    def street(self):
        with allure.step("Улица"):
            self.driver.find_element_by_name("legal[street]").clear()
            return self.driver.find_element_by_name("legal[street]")

    @property
    def house(self):
        with allure.step("Дом/Офис"):
            self.driver.find_element_by_name("legal[house]").clear()
            return self.driver.find_element_by_name("legal[house]")

    @property
    def head_last_name(self):
        with allure.step("Фамилия руководителя"):
            self.driver.find_element_by_name("head_last_name").clear()
            return self.driver.find_element_by_name("head_last_name")

    @property
    def head_first_name(self):
        with allure.step("Имя руководителя"):
            self.driver.find_element_by_name("head_first_name").clear()
            return self.driver.find_element_by_name("head_first_name")

    @property
    def head_middle_name(self):
        with allure.step("Отчество руководителя"):
            self.driver.find_element_by_name("head_middle_name").clear()
            return self.driver.find_element_by_name("head_middle_name")

    @property
    def head_job(self):
        with allure.step("Долножсть руководителя"):
            self.driver.find_element_by_name("head_job").clear()
            return self.driver.find_element_by_name("head_job")

    @property
    def choose_activities_button(self):
        with allure.step("Перечень сферы дейтельности кнопка выбрать"):
            return self.driver.find_element_by_xpath(
                "//table[@class='x-btn tree_selector_choose_btn x-btn-noicon']//button[.='Добавить']")

    @property
    def list_actitivities_select(self):
        with allure.step("Выбрать в списке сфер дейтельности"):
            return self.driver.find_element_by_xpath(
                "//table[@class='x-btn tree_window_select_btn x-btn-noicon']//button[.='Выбрать']")

    @property
    def offered_products(self):
        with allure.step("Предлагаемые услуги и продукция"):
            self.driver.find_element_by_name("offered_products").clear()
            return self.driver.find_element_by_name("offered_products")

    @property
    def checking_account(self):
        with allure.step("Рассчетный счет"):
            self.driver.find_element_by_name("account").clear()
            return self.driver.find_element_by_name("account")

    @property
    def bik(self):
        with allure.step("БИК"):
            self.driver.find_element_by_name("bik").clear()
            return self.driver.find_element_by_name("bik")

    @property
    def bank_name(self):
        with allure.step("Название банка"):
            self.driver.find_element_by_name("bank").clear()
            return self.driver.find_element_by_name("bank")

    @property
    def bank_adress(self):
        with allure.step("Адрес банка"):
            self.driver.find_element_by_name("bank_addr").clear()
            return self.driver.find_element_by_name("bank_addr")

    @property
    def accept_processing(self):
        with allure.step("Даю согласие на обработку данных Чек-бокс"):
            return self.driver.find_element_by_name("accept_processing")

    @property
    def register_button(self):
        with allure.step("Кнопка Зарегистрироваться"):
            return self.button("Зарегистрироваться")

    @Helper.wait_for_ajax()
    def confirm_button(self):
        with allure.step("Подтвердить"):
            self.button("Подтвердить").click()

    @Helper.wait_for_ajax()
    def bank_details(self, account="30101810400000000225", bik="044525225"):
        if self.type_company == 3:
            self.bik.click()
            self.button('ОК').click()
        self.checking_account.send_keys(f"{account}")
        self.bik.send_keys(f"{bik}")

    @Helper.wait_for_ajax()
    def accept_and_register(self):
        with allure.step("Согласие на обработку данных и регистрация"):
            self.accept_processing.click()
            time.sleep(1)
            self.register_button.click()

    @Helper.wait_for_ajax()
    def service_products_offered(self):
        """Только для Участников закупки"""
        pass

    @Helper.wait_for_ajax()
    def information_about_head(self, last_name="Андреев", first_name="Павел", middle_name="Отчество",
                               job="Генеральный директор"):
        with allure.step(f"Информация о руководителе компании: {last_name, first_name, middle_name, job} "):
            self.head_last_name.send_keys(last_name)
            self.head_first_name.send_keys(first_name)
            self.head_middle_name.send_keys(middle_name)
            self.head_job.send_keys(job)

    @Helper.wait_for_ajax()
    def fill_legal_adress(self, index=125003, region="Моск", city="Moscow", street="Большая якиманка",
                          house="д.24 офис 5"):
        self.postcode.send_keys(f"{index}")
        self.region.send_keys(f"{region}")
        self.driver.find_element_by_xpath(f"//div[.='Москва']").click()
        self.city.send_keys(f"{city}")
        self.street.send_keys(f"{street}")
        self.house.send_keys(f"{house}")

    @Helper.wait_for_ajax()
    def fill_general_phone(self, phone):
        with allure.step(f"Заполнение телефона организации {phone}"):
            tel = str(phone)
            self.general_phone_country_code.send_keys(tel[:1])
            self.general_phone_city_code.send_keys(tel[1:4])
            self.general_phone_number.send_keys(tel[4:])

    @Helper.wait_for_ajax()
    def fill_general_email(self, email):
        """Передать только название почты без @ """
        with allure.step(f"Заполнения Адреса Электронной почты {email}"):
            self.general_email.send_keys(f"{email}")

    @Helper.wait_for_ajax()
    def fill_contact_organization(self, email="Test_mail", phone=84956857404):
        with allure.step("Заполнение контактных данных Организации"):
            self.fill_general_email(email)
            self.fill_general_phone(phone)

    @Helper.wait_for_ajax()
    def fill_okpo(self, okpo="93281776"):
        with allure.step("Заполнение ОКПО"):
            if self.role == 1:
                if self.type_company != 2:
                    self.okpo.send_keys(f"{okpo}")
            else:
                pass

    @Helper.wait_for_ajax()
    def fill_data_organization(self, inn, kpp, ogrn):
        with allure.step(f"Заполнение данных организации ИНН , КПП , ОГРН"):
            with allure.step(f"ИНН: {inn}"):
                self.inn.send_keys(inn)
                if self.type_company == 1:
                    with allure.step(f"КПП: {kpp}"):
                        self.kpp.send_keys(kpp)
                    with allure.step(f"ОГРН {ogrn}"):
                        self.ogrn.send_keys(ogrn)
                elif self.type_company == 3:
                    with allure.step(f"ОГРН {ogrn}"):
                        self.ogrn.send_keys(ogrn + str(random.randint(10, 99)))
                elif self.type_company == 2:
                    pass

    @Helper.wait_for_ajax()
    def fill_register_date(self):
        with allure.step("Заполнение даты постановки в налоговый учет"):
            if self.role == 1:
                self.registration_date.send_keys(datetime.date.today().strftime("%d.%m.%y"))
            else:
                pass

    @Helper.wait_for_ajax()
    def fill_name_organization(self, name):
        if self.type_company == 3:
            with allure.step(f"Указание организации ИП: {name['name_IP']}"):
                self.name_organization.send_keys(f"{name['name_IP']}")
                self.short_name_organization.send_keys(name['name_IP'])
        else:
            with allure.step(f"Указание полного наименования организации {name['name_company']}"):
                self.name_organization.send_keys(name['name_company'])
                self.short_name_organization.send_keys(name['name_company'])