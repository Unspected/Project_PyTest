import allure

from Page.helper import Helper
from Page.registration.register_organization.sng_resident_base import BaseOrganizationDetailsSNG


class OrganizationDetailProviderSNG(BaseOrganizationDetailsSNG):
    def __init__(self, driver):
        super().__init__(driver)

    @Helper.wait_for_ajax()
    def service_products_offered(self):
        with allure.step("Выбор оказываемых услуг и продукции"):
            self.choose_activities_button.click()
            self.span_text("B ПРОДУКЦИЯ ГОРНОДОБЫВАЮЩИХ ПРОИЗВОДСТВ").click()
            self.list_actitivities_select.click()
            self.offered_products.send_keys("Предлагаемая продукция и товары поставщика")