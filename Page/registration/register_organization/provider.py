import allure

from Page.helper import Helper
from Page.login_page import LoginPage
from Page.main_page import MainPage
from Page.registration.register_organization.base import BaseOrganizationDetails
from Values.members import Members


class OrganizationDetailsProvider(BaseOrganizationDetails):
    def __init__(self, driver):
        super().__init__(driver)

    @property
    def legal_form_button(self):
        """Селектор только для поставщика"""
        with allure.step("Организационно-правовая форма (Для поста)"):
            return self.driver.find_element_by_xpath(
                "//table[@class='x-btn x-btn-noicon x-box-item']//button[.='Выбрать']")

    @Helper.wait_for_ajax()
    def service_products_offered(self):
        with allure.step("Выбор оказываемых услуг и продукции"):
            self.choose_activities_button.click()
            self.span_text("B ПРОДУКЦИЯ ГОРНОДОБЫВАЮЩИХ ПРОИЗВОДСТВ").click()
            self.list_actitivities_select.click()
            self.offered_products.send_keys("Предлагаемая продукция и товары поставщика")

    @Helper.wait_for_ajax()
    def fill_legal_form(self):
        """Метод только для поставщика Выбор Оргазницинной правовой формы"""
        if self.type_company == 1:
            with allure.step("Выбор Организационно-правовой формы"):
                self.legal_form_button.click()
                self.span_text("12200 Акционерные общества").click()
                self.driver.find_element_by_xpath("//span[.='Справочник ОКОПФ']/following::button[.='Выбрать']").click()
        else:
            pass