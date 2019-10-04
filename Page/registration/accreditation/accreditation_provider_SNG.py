import allure

from Page.helper import Helper
from Page.main_page import MainPage
from Page.registration.accreditation.accreditation_Base_SNG import AccreditationBaseSNG


class AccreditationProviderSNG(AccreditationBaseSNG):
    def __init__(self, driver):
        super().__init__(driver)

    def prepare_docs_for_accreditation(self, value):
        MainPage(self.driver).view_organization_data()
        self.wait.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")
        self.wait.until(lambda driver: self.supplier_accreditation_btn).click()
        self.register_as_supplier.click()
        # Документы регистрации
        self.attach_accreditation_documents(value)
        self.accreditation_completing()

    @Helper.wait_for_ajax()
    def attach_accreditation_documents(self, value):
        if value["type_company"] == 1:
            self.legal_documents_accreditation()
        elif value["type_company"] == 2:
            self.individual_documents_accreditation()

    @Helper.wait_for_ajax()
    def legal_documents_accreditation(self):
        with allure.step("Документы для аккредитации ЮРИДИЧЕСКОГО ЛИЦА"):
            self.attach_file_accreditation("Копия свидетельства о государственной регистрации", "Копия")
            self.attach_file_accreditation(
                "Заявление о присоединении к Регламенту организации и проведения закупочных процедур в электронной форме",
                "Заявление")

    @Helper.wait_for_ajax()
    def individual_documents_accreditation(self):
        with allure.step("Документы для аккредитации ИНДВИДУАЛЬНОГО ПРЕДПРИНИМАТЕЛЯ"):
            self.attach_file_accreditation("Копия свидетельства о государственной регистрации ИП", "Копия ИП")
            self.attach_file_accreditation(
                "Заявление о присоединении к Регламенту организации и проведения закупочных процедур в электронной форме",
                "Заявление")
