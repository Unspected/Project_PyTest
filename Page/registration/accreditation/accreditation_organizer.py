
import allure
from Page.helper import Helper
from Page.registration.accreditation.accreditation_customer import AccreditationCustomer


class AccreditationOrganizer(AccreditationCustomer):
    def __init__(self, driver):
        super().__init__(driver)

    @Helper.wait_for_ajax()
    def attach_documents_customer(self):
        with allure.step("Документы для аккредитации Организатора"):
            self.attach_file_accreditation("Копии документов, подтверждающих полномочия руководителя",
                                           "Копия документа")
            self.attach_file_accreditation(
                "Копии документов, подтверждающих полномочия лица на регистрацию и осуществление действий от имени Заказчика / Организатора",
                "Копии доков")
