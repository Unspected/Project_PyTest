from Page.helper import Helper
from Page.main_page import MainPage
from Page.registration.accreditation.accreditation_provider_SNG import AccreditationProviderSNG


class AccreditationForeignProvider(AccreditationProviderSNG):
    def __init__(self, driver):
        super().__init__(driver)

    @Helper.wait_for_ajax()
    def accept_register_contragents(self, value):
        list = {1: "Участники закупки (другие страны)"}
        MainPage(self.driver).organization.click()
        self.move_to(MainPage(self.driver).app_for_registration)
        self.span_text(f"{list[value['role']]}").click()