import allure

from Page.helper import Helper
from Page.registration.register_organization.sng_resident_base import BaseOrganizationDetailsSNG


class BaseOrganizationDetailsForeign(BaseOrganizationDetailsSNG):
    def __init__(self, driver):
        super().__init__(driver)

    def choose_role_in_system(self, role):
        pass

    @Helper.wait_for_ajax()
    def select_type_company(self, type):
        """
        :param type: int по типу в массиве
        :return:
        """
        company = {
            1: "Юридическое лицо (другие страны)",
            2: "Индивидуальный предприниматель (другие страны)"
        }
        with allure.step(f"Выбран тип компании {company[type]}"):
            self.type_of_company.click()
            self.driver.find_element_by_xpath(f"//div[@class='x-combo-list-inner']/div[.='{company[type]}']").click()
            self.type_company = type

    @property
    def type_of_company(self):
        return self.driver.find_element_by_xpath("//input[@name='supplier_profile_id']/../img")

    @Helper.wait_for_ajax()
    def service_products_offered(self):
        with allure.step("Выбор оказываемых услуг и продукции"):
            self.choose_activities_button.click()
            self.span_text("B ПРОДУКЦИЯ ГОРНОДОБЫВАЮЩИХ ПРОИЗВОДСТВ").click()
            self.list_actitivities_select.click()
            self.offered_products.send_keys("Предлагаемая продукция и товары поставщика")