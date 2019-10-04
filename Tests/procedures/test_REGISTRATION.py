from Values.registration.base import BaseRegisterValue


# ПЕРЕД ВЫПОЛНЕНИЕМ НА ПЛОЩАДКЕ НЕ ОБХОДИМО ВЫБРУИТЬ ПРИМУ В КОНФИГАХ
# Для предпрода
# В БД ВЫПОЛНИТЬ ЗАПРОС update surveys
# set actual = false
# where id in (1,3,4,5,6,7,8,9)

@allure.parent_suite("Регистрация")
@pytest.mark.usefixtures("chrome_driver")
class TestRegistration:

    @allure.suite("Регистрация Поставщика РФ")
    @pytest.mark.parametrize("new_user", [
        BaseRegisterValue(role=1, type_company=1).new_user_RF,
        BaseRegisterValue(role=1, type_company=2).new_user_RF,
        BaseRegisterValue(role=1, type_company=3).new_user_RF])
    def test_provider(self, new_user):
        OrganizationDetailsProvider(self.driver).registration_page(new_user)
        AccreditationProvider(self.driver).accreditation_user(new_user)

    @allure.suite("Регистрация Заказчика РФ")
    @pytest.mark.parametrize("new_user", [
        BaseRegisterValue(role=2, type_company=1).new_user_RF,
        BaseRegisterValue(role=2, type_company=2).new_user_RF,
        BaseRegisterValue(role=2, type_company=3).new_user_RF])
    def test_customer(self, new_user):
        OrganizationDetailsCustomer(self.driver).registration_page(new_user)
        AccreditationCustomer(self.driver).accreditation_user(new_user)

    @allure.suite("Регистрация Организатора РФ")
    @pytest.mark.parametrize("new_user", [
        BaseRegisterValue(role=3, type_company=1).new_user_RF,
        BaseRegisterValue(role=3, type_company=2).new_user_RF,
        BaseRegisterValue(role=3, type_company=3).new_user_RF])
    def test_organizator(self, new_user):
        OrganizationDetailsOrganizator(self.driver).registration_page(new_user)
        AccreditationOrganizer(self.driver).accreditation_user(new_user)

    @allure.suite("Регистрация Поставщика СНГ")
    @pytest.mark.parametrize("new_user", [
        BaseRegisterValue(role=1, type_company=1).new_user_SNG,
        BaseRegisterValue(role=1, type_company=2).new_user_SNG])
    def test_provider_sng(self, new_user):
        OrganizationDetailProviderSNG(self.driver).registration_page(new_user)
        AccreditationProviderSNG(self.driver).accreditation_user(new_user)

    @allure.suite("Регистрация Заказчика СНГ")
    @pytest.mark.parametrize("new_user", [
        BaseRegisterValue(role=2, type_company=1).new_user_SNG,
        BaseRegisterValue(role=2, type_company=2).new_user_SNG])
    def test_customer_sng(self, new_user):
        BaseOrganizationDetailsSNG(self.driver).registration_page(new_user)
        AccreditationCustomerSNG(self.driver).accreditation_user(new_user)

    @allure.suite("Регистрация Поставщика Иностранец")
    @pytest.mark.parametrize("new_user", [
        BaseRegisterValue(role=1, type_company=1).new_user_foreign,
        BaseRegisterValue(role=1, type_company=2).new_user_foreign])
    def test_provider_foreign(self, new_user):
        BaseOrganizationDetailsForeign(self.driver).registration_page(new_user)
        AccreditationForeignProvider(self.driver).accreditation_user(new_user)
