import allure
import time
from Page.base import BaseProcedures
from Page.helper import Helper
from Page.login_page import LoginPage
from Page.main_page import MainPage
from Page.registration.base_registration import BaseRegistration
from Page.registration.register_organization.base import BaseOrganizationDetails
from Values.members import Members


class AccreditationBase(BaseRegistration):
    def __init__(self, driver):
        super().__init__(driver)

    @Helper.wait_for_ajax()
    def accreditation_user(self, value, solution=1):
        LoginPage(self.driver).login(value)
        self.prepare_docs_for_accreditation(value)
        LoginPage(self.driver).logout()
        LoginPage(self.driver).login(Members().ADMIN_ETP)
        self.accept_register_contragents(value)
        self.search_new_accreditation_company(value)
        self.confirm_registration(value, solution)
        LoginPage(self.driver).logout()

    @Helper.wait_for_ajax()
    def prepare_docs_for_accreditation(self, *args):
        """Аккредитация для разных ролей"""
        pass

    @Helper.wait_for_ajax()
    def accept_register_contragents(self, value):
        list = {1: "Участники закупки (РФ)", 2: "Заказчики (РФ)", 3: "Заказчики (РФ)"}
        MainPage(self.driver).organization.click()
        self.move_to(MainPage(self.driver).app_for_registration)
        self.span_text(f"{list[value['role']]}").click()

    @Helper.wait_for_ajax()
    def search_new_accreditation_company(self, value):
        with allure.step("Поиск компании для аккредитации "):
            MainPage(self.driver).advanced_search.click()
            MainPage(self.driver).search_email_input.send_keys(value["general_email"])
            MainPage(self.driver).inn.send_keys(value["inn"])
            MainPage(self.driver).search_advanced_btn.click()
            self.assertion_result_search(value)
            self.wait.until(lambda driver: MainPage(self.driver).review_company_btn).click()

    @Helper.wait_for_ajax()
    def assertion_result_search(self, value):
        with allure.step("Результаты поиска"):
            time.sleep(0.5)
            inn = self.driver.find_element_by_xpath(
                "//div[contains(@class,'x-grid3-cell-inner x-grid3-col-3')]").get_attribute("textContent")
            email = self.driver.find_element_by_xpath(
                "//div[contains(@class,'x-grid3-cell-inner x-grid3-col-5')]").get_attribute("textContent")
            assert inn == value["inn"]
            assert email == value["general_email"]

    @property
    def full_name_valid(self):
        with allure.step("Наименование организации чек-бокс"):
            return self.driver.find_element_by_name("full_name_valid")

    @property
    def short_name_valid(self):
        with allure.step("Краткое наименование организации чек-бокс"):
            return self.driver.find_element_by_name("short_name_valid")

    @property
    def inn_valid(self):
        with allure.step("ИНН валидный чек-бокс"):
            return self.driver.find_element_by_name("inn_valid")

    @property
    def ogrn_valid(self):
        with allure.step("ОГРН валидный чек-бокс"):
            return self.driver.find_element_by_name("ogrn_valid")

    @property
    def legal_address_valid(self):
        with allure.step("Юридический адрес чек-бокс"):
            return self.driver.find_element_by_name("legal_address_valid")

    @property
    def no_valid_documents(self):
        with allure.step(
                "Предоставление документов, не соответствующих требованиям, установленным законодательством Российской Федерации"):
            return self.driver.find_element_by_id("nonvalidInfo")

    @property
    def copy_document_header(self):
        with allure.step("Копии документов, подтверждающих полномочия руководителя"):
            return self.driver.find_element_by_id('check_0')

    @property
    def copy_document_accreditation(self):
        with allure.step(
                "Копии документов, подтверждающих полномочия лица на регистрацию и осуществление действий от имени Заказчика"):
            return self.driver.find_element_by_id("check_1")

    @Helper.wait_for_ajax()
    def confirm_registration(self, value, solution=1):
        """
        :param solution: 1 - Подписать одобрение аккредитации 2 - Отказ
        :return:
        """
        self.wait.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")
        if solution == 1:
            with allure.step("Подтверждение регистрации"):
                self.check_register_data(value)
                self.full_name_valid.click()
                self.short_name_valid.click()
                self.inn_valid.click()
                self.ogrn_valid.click()
                self.legal_address_valid.click()
                assert self.full_name_valid.is_selected(), "Чек-бокс не установлен "
                assert self.short_name_valid.is_selected(), "Чек-бокс не установлен"
                assert self.inn_valid.is_selected(), "Чек-бокс не установлен"
                assert self.ogrn_valid.is_selected(), "Чек-бокс не установлен"
                assert self.legal_address_valid.is_selected(), "Чек-бокс не установлен"
                self.driver.find_element_by_xpath(
                    f"//span[.='Подтверждение регистрации']/following::button[.='Подписать'][1]").click()
                self.wait.until(lambda driver: self.button('ОК')).click()
        elif solution == 2:
            with allure.step("Отклонение аккредитации"):
                self.no_valid_documents.click()
                self.copy_document_header.click()
                self.copy_document_accreditation.click()
                self.driver.find_element_by_xpath(
                    "//span[.='Подтверждение регистрации']/following::button[.='Подписать'][2]").click()
                assert self.wait.until(lambda driver: self.span_text("Заявка отклонена")).is_displayed()
                self.wait.until(lambda driver: self.button('ОК')).click()

    @Helper.wait_for_ajax()
    def check_register_data(self, value):
        name_company_valid = self.driver.find_element_by_xpath(f"//label[@for='checkbox0']").text
        name_company_valid = name_company_valid.split(': ')[1]

        inn = self.driver.find_element_by_xpath(f"//label[@for='checkbox2']").text
        inn = inn.split(': ')[1]

        ogrn = self.driver.find_element_by_xpath(f"//label[@for='checkbox3']").text
        ogrn = ogrn.split(': ')[1]

        legal_address = self.driver.find_element_by_xpath(f"//label[@for='checkbox4']").text
        legal_address = legal_address.split(': ')[1]

        full_address = f"{value['index']}, Российская Федерация, {value['region']}, {value['city']}, {value['street']}, {value['house']}"

        if value['type_company'] == 1:
            with allure.step("Тип компании ЮР лицо"):
                self.assertion(value["name_company"], name_company_valid, "Сравнение название компании")
                self.assertion(value['inn'] + '/' + value['kpp'], inn, "Сравнение ИНН/КПП")
                self.assertion(value['ogrn'], ogrn, "Сравнение ОГРН")
        elif value['type_company'] == 2:
            with allure.step("Тип компании Физ лицо"):
                self.assertion(value["name_company"], name_company_valid, "Сравнение название компании")
                self.assertion(value['inn'], inn[:-5], "Сравнение ИНН")
                self.assertion("отсутствует", ogrn, "Сравнение ОГРН")
        elif value['type_company'] == 3:
            with allure.step("Тип компании Индивидуальный предприниматель"):
                self.assertion(value["name_IP"], name_company_valid, "Сравнение название компании")
                self.assertion(value['inn'], inn[:-5], "Сравнение ИНН")
                self.assertion(value['ogrn'], ogrn[:-2], "Сравнение ОГРН")
        self.assertion(full_address, legal_address, "Сравнение адресов")
