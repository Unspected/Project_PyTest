import time
import allure
from Page.helper import Helper
from Page.main_page import MainPage
from Page.registration.accreditation.accreditaion_base import AccreditationBase


class AccreditationProvider(AccreditationBase):
    def __init__(self, driver, ):
        super().__init__(driver)

    def prepare_docs_for_accreditation(self, value):
        self.notice_edo(value)
        MainPage(self.driver).view_organization_data()
        self.wait.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")
        self.wait.until(lambda driver: self.supplier_accreditation_btn).click()
        self.register_as_supplier.click()
        # Документы регистрации
        self.check_type_of_company(value)
        self.attach_accreditation_documents(value)
        self.accreditation_completing()

    @property
    def promo_edo(self):
        with allure.step("Уведомление ЭДО"):
            return self.driver.find_element_by_xpath("//span[.='Внимание']")

    @property
    def close_notice(self):
        with allure.step("Закрыть уведомление"):
            return self.driver.find_element_by_xpath("//div[@class='x-tool x-tool-close']")

    @property
    def agree_edo(self):
        with allure.step("Согласен получать бухгалтерские доки"):
            return self.driver.find_element_by_name("agree")

    @property
    def supplier_accreditation_btn(self):
        with allure.step("Аккредитация поставщика кнопка"):
            return self.button("Аккредитация поставщика")

    @property
    def register_as_supplier(self):
        with allure.step("Регистрация в качестве участника закупки"):
            return self.driver.find_element_by_xpath(
                "//span[@class='x-tab-strip-inner']/span[.='Регистрация в качестве участника закупки']")

    @property
    def type_company_accreditation(self):
        # Ассертов с гет аттрибута value
        return self.driver.find_element_by_name("supplier_profile_id")

    @property
    def max_contract_price(self):
        with allure.step("Максимальная сумма, руб."):
            return self.driver.find_element_by_name("max_contract_price")

    @property
    def fast_reg_offer(self):
        with allure.step("Чек-бокс Ускоренная аккредитация"):
            return self.driver.find_element_by_name("fast_reg_offer")

    @property
    def sign_forward(self):
        with allure.step("Кнопка подписать и направить"):
            return self.button("Подписать и направить")

    @property
    def type_of_company(self):
        with allure.step("Тип компании"):
            return self.driver.find_element_by_name("supplier_profile_id")

    @Helper.wait_for_ajax()
    def check_type_of_company(self, value):
        with allure.step("Проверка типа компании"):
            self.wait.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")
            assert int(self.type_of_company.get_attribute('value')) == value["type_company"]

    @Helper.wait_for_ajax()
    def accreditation_completing(self):
        with allure.step("Завершение аккредитации Поставщика"):
            self.fast_reg_offer.click()
            self.sign_forward.click()
            self.button('ОК').click()
            self.wait_supplier_signature_text()
            self.button('Подписать').click()
            self.button('Да').click()
            self.button('ОК').click()

    @Helper.wait_for_ajax()
    def fill_max_contract_price(self, price="9999991"):
        with allure.step("Максимально возможная сумма для заключения контракта (договора)"):
            self.max_contract_price.send_keys(f'{price}')

    @Helper.wait_for_ajax()
    def notice_edo(self, value):
        with allure.step("Уведомление ЭДО (только для поставщиков) не ФИЗ ЛИЦ"):
            if value["type_company"] == 2:
                pass
            else:
                self.wait.until(lambda driver: self.promo_edo)
                self.close_notice.click()
                self.agree_edo.click()
                self.button("Подтвердить").click()
                self.button("ОК").click()

    @Helper.wait_for_ajax()
    def attach_accreditation_documents(self, value):
        if value["type_company"] == 1:
            self.legal_documents_accreditation()
        elif value["type_company"] == 2:
            self.physical_documents_accreditation()
        elif value["type_company"] == 3:
            self.individual_documents_accreditation()

    @Helper.wait_for_ajax()
    def legal_documents_accreditation(self):
        with allure.step("Документы для аккредитации ЮРИДИЧЕСКОГО ЛИЦА"):
            self.attach_file_accreditation("Копия выписки из ЕГРЮЛ", "ЕГРЮЛ")
            self.attach_file_accreditation("Копия учредительных документов участника закупки", "Участник закупки")
            self.attach_file_accreditation("Копии документов, подтверждающих полномочия лица на получение аккредитации",
                                           "Полномочия лица")
            self.attach_file_accreditation("Копии документов, подтверждающих полномочия руководителя", "Руководитель")
            self.attach_file_accreditation(
                "Решение об одобрении или о совершении по результатам электронных процедур сделок от имени участника закупки",
                "Сделки")
            self.fill_max_contract_price()

    @Helper.wait_for_ajax()
    def physical_documents_accreditation(self):
        with allure.step("Документы для аккредитации ФИЗИЧЕСКОГО ЛИЦА"):
            self.attach_file_accreditation("Копия свидетельства о присвоении ИНН", "ИНН")
            self.attach_file_accreditation("Копии документов, удостоверяющих личность", "Удостоверение личности")

    @Helper.wait_for_ajax()
    def individual_documents_accreditation(self):
        with allure.step("Документы для аккредитации ИНДВИДУАЛЬНОГО ПРЕДПРИНИМАТЕЛЯ"):
            self.attach_file_accreditation("Копия выписки из ЕГРИП", "ЕГРИП")
            self.attach_file_accreditation("Копии документов, удостоверяющих личность", "Удостоверящие личность")
