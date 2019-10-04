import time

import allure

from Page.helper import Helper
from Page.main_page import MainPage
from Page.registration.accreditation.accreditation_provider import AccreditationProvider


class AccreditationBaseSNG(AccreditationProvider):
    def __init__(self, driver):
        super().__init__(driver)

    @Helper.wait_for_ajax()
    def accept_register_contragents(self, value):
        list = {1: "Участники закупки (СНГ)", 2: "Заказчики (СНГ)"}
        MainPage(self.driver).organization.click()
        self.move_to(MainPage(self.driver).app_for_registration)
        self.span_text(f"{list[value['role']]}").click()


    @property
    def state_account_number_valid(self):
        with allure.step("Государственный регистрационный номер"):
            return self.driver.find_element_by_name("state_account_number_valid")

    @property
    def tin_valid(self):
        with allure.step("Идентификационный номер налогоплательщика (TIN)"):
            return self.driver.find_element_by_name("tin_valid")

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
                self.state_account_number_valid.click()
                self.tin_valid.click()
                self.legal_address_valid.click()
                assert self.full_name_valid.is_selected(), "Чек-бокс не установлен "
                assert self.short_name_valid.is_selected(), "Чек-бокс не установлен"
                assert self.state_account_number_valid.is_selected(), "Чек-бокс не установлен"
                assert self.tin_valid.is_selected(), "Чек-бокс не установлен"
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

        register_number = self.driver.find_element_by_xpath(f"//label[@for='checkbox2']").text
        register_number = register_number.split(': ')[1]

        tin = self.driver.find_element_by_xpath(f"//label[@for='checkbox3']").text
        tin = tin.split(': ')[1]

        legal_address = self.driver.find_element_by_xpath(f"//label[@for='checkbox4']").text
        legal_address = legal_address.split(': ')[1]

        full_address = f"{value['index']}, {value['country']}, {value['region']}, {value['city']}, {value['street']}, {value['house']}"

        self.assertion(value["name_company"], name_company_valid, "Сравнение название компании")
        self.assertion(value['register_number'], register_number, "Регистрационного номера")
        self.assertion(value['tin'], tin, "Сравнение ОГРН")
        self.assertion(full_address, legal_address, "Сравнение адресов")
