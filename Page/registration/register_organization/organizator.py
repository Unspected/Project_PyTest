import allure

from Page.helper import Helper
from Page.login_page import LoginPage
from Page.main_page import MainPage
from Page.registration.register_organization.base import BaseOrganizationDetails


class OrganizationDetailsOrganizator(BaseOrganizationDetails):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def legal_form_button(self):
        with allure.step("Организационно правовая форма"):
            return self.driver.find_element_by_xpath(
                "//input[@class='x-form-text x-form-field x-form-empty-field x-trigger-noedit']")

    @property
    def customer_type(self):
        with allure.step("Субъект 223ФЗ"):
            return self.driver.find_element_by_name("customer_type")

    @Helper.wait_for_ajax()
    def fill_legal_form(self):
        with allure.step("Выбор организационой правой формы для Юридического лица"):
            if self.type_company == 1:
                self.legal_form_button.click()
                self.driver.find_element_by_xpath("//div[.='Другая форма']").click()
            else:
                pass