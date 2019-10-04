from Page.registration.accreditation.accreditaion_base import AccreditationBase
import time
import allure
from Page.helper import Helper


class AccreditationCustomer(AccreditationBase):
    def __init__(self, driver):
        super().__init__(driver)

    def prepare_docs_for_accreditation(self, value):
        self.wait.until(lambda driver: self.driver.execute_script("return document.readyState") == "complete")
        self.use_eds.click()
        self.attach_documents_customer()
        self.send_review.click()
        self.signature_text_customer()

    @property
    def use_eds(self):
        with allure.step("Включить использование ЭП"):
            return self.driver.find_element_by_name("use_eds")

    @property
    def send_review(self):
        with allure.step("Отправить на рассмотрение"):
            return self.button("Отправить на рассмотрение")

    @Helper.wait_for_ajax()
    def attach_documents_customer(self):
        with allure.step("Документы для аккредитации Заказчика"):
            self.attach_file_accreditation("Копии документов, подтверждающих полномочия руководителя", "Копия документа")
            self.attach_file_accreditation(
                "Копии документов, подтверждающих полномочия лица на регистрацию и осуществление действий от имени Заказчика",
                "Копии доков")

    @Helper.wait_for_ajax()
    def signature_text_customer(self):
        with allure.step("Подтверждение и подписание данных перед отправкой на аккредитацию"):
            self.wait_signature_text()
            self.button("Подписать").click()
            self.button('ОК').click()
