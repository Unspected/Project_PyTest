from Page.helper import Helper
import allure
import time
from Page.registration.base_registration import BaseRegistration
from Page.registration.register_organization.base import BaseOrganizationDetails


class BaseOrganizationDetailsSNG(BaseOrganizationDetails):
    def __init__(self, driver):
        super().__init__(driver)

    @Helper.wait_for_ajax()
    def fill_organizator_info(self, value):
        with allure.step("Заполнение данных об контрагента СНГ"):
            self.select_type_company(value["type_company"])
            self.fill_name_organization(value)
            self.main_details(value)
            self.fill_contact_organization(value["general_email"], value["general_phone"])
            self.fill_legal_adress(value)
            self.information_about_head(value["last_name"], value["first_name"], value["middle_name"], value["job"])
            self.service_products_offered()
            self.bank_details(value)
            self.register_complete()

    @Helper.wait_for_ajax()
    def select_type_company(self, type):
        """
        :param type: int по типу в массиве
        :return:
        """
        company = {
            1: "Юридическое лицо (СНГ)",
            2: "Индивидуальный предприниматель (СНГ)"
        }
        with allure.step(f"Выбран тип компании {company[type]}"):
            self.type_of_company.click()
            self.driver.find_element_by_xpath(f"//div[@class='x-combo-list-inner']/div[.='{company[type]}']").click()
            self.type_company = type

    @property
    def type_of_company(self):
        with allure.step("Тип компании СНГ"):
            return self.driver.find_element_by_xpath(
                "//div[@class='x-form-field-wrap x-form-field-trigger-wrap']//input[@class='x-form-text x-form-field x-trigger-noedit']")

    @property
    def state_account_number(self):
        with allure.step("Государственный регистрационный номер в стране регистрации"):
            self.driver.find_element_by_name("state_account_number").clear()
            return self.driver.find_element_by_name("state_account_number")

    @property
    def tin(self):
        with allure.step("Идентификационный номер налогоплательщика (TIN)"):
            self.driver.find_element_by_name("tin").clear()
            return self.driver.find_element_by_name("tin")

    @property
    def country(self):
        with allure.step("Страна"):
            self.driver.find_element_by_xpath("//input[@name='legal[country_iso_nr]']/../input[2]").clear()
            return self.driver.find_element_by_xpath("//input[@name='legal[country_iso_nr]']/../input[2]")

    @property
    def beneficiary_iban(self):
        with allure.step("IBAN"):
            self.driver.find_element_by_name("beneficiary_iban").clear()
            return self.driver.find_element_by_name("beneficiary_iban")

    @property
    def beneficiary_account(self):
        with allure.step("Счет №"):
            self.driver.find_element_by_name("beneficiary_account").clear()
            return self.driver.find_element_by_name("beneficiary_account")

    @property
    def beneficiary_bank_name(self):
        with allure.step("Наименование"):
            self.driver.find_element_by_name("beneficiary_bank_name").clear()
            return self.driver.find_element_by_name("beneficiary_bank_name")

    @property
    def beneficiary_bank_swift(self):
        with allure.step("SWITFT code"):
            self.driver.find_element_by_name("beneficiary_bank_swift").clear()
            return self.driver.find_element_by_name('beneficiary_bank_swift')

    @property
    def confirm_data_checkbox(self):
        with allure.step("Настоящим подтверждаю корректность введённых мною данных"):
            return self.driver.find_element_by_xpath("//input[@type='checkbox'][not(@checked)]")

    @Helper.wait_for_ajax()
    def bank_details(self, value):
        with allure.step("Банковские реквизиты"):
            self.beneficiary_iban.send_keys(value["iban"])
            self.beneficiary_account.send_keys(value["bank_account"])
            self.beneficiary_bank_name.send_keys(value["bank_name"])
            self.beneficiary_bank_swift.send_keys(value["bank_swift"])

    @Helper.wait_for_ajax()
    def register_complete(self, file="ETP_SNG.pdf"):
        with allure.step("Завершение регистрации"):
            self.confirm_data_checkbox.click()
            self.driver.find_element_by_xpath("//input[@type='file']").send_keys(self.get_file(file))
            self.wait.until(
                lambda driver: self.driver.find_element_by_link_text("Заявление о присоединении к Регламенту"))
            self.button('Зарегистрироваться').click()
            self.wait_signature_text()
            self.button('Подтвердить').click()

    @Helper.wait_for_ajax()
    def fill_legal_adress(self, value):
        self.country.send_keys(value["country"])
        self.driver.find_element_by_xpath(f"//div[contains(text(),'{value['country']}')]").click()
        self.postcode.send_keys(f"{value['index']}")
        self.region.send_keys(f"{value['region']}")
        self.city.send_keys(f"{value['city']}")
        self.street.send_keys(f"{value['street']}")
        self.house.send_keys(f"{value['house']}")

    @Helper.wait_for_ajax()
    def main_details(self, value):
        with allure.step(f"Государственный регистрационный номер в стране регистрации: {value['register_number']}"):
            self.state_account_number.send_keys(value["register_number"])
        with allure.step(f"Идентификационный номер налогоплательщика (TIN): {value['tin']}"):
            self.tin.send_keys(value["tin"])
        with allure.step(f"ИНН в РФ: {value['inn']}"):
            self.inn.send_keys(value["inn"])
