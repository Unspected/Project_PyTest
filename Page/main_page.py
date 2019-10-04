import allure
from Page.helper import Helper
from Page.base import BaseProcedures


class MainPage(BaseProcedures):

    @property
    def procedures_btn(self):
        return self.button("Процедуры")

    @property
    def procedures_ptype_btn(self):
        return self.button("Продажа и аренда имущества")

    @property
    def administration_btn(self):
        return self.button("Администрирование")

    @property
    def journal_btn(self):
        return self.span_text("Журналы")

    @property
    def mail_notification(self):
        return self.span_text("Почтовые уведомления")

    @property
    def advanced_search(self):
        return self.button("Расширенный поиск")

    @property
    def search_email_input(self):
        return self.driver.find_element_by_name("email")

    @property
    def not_sent_mails(self):
        return self.driver.find_element_by_xpath("//input[@name='is_datetime_sent'][@value=0]")

    @property
    def search_advanced_btn(self):
        with allure.step("Кнопка искать в Расширенном поиске"):
            return self.driver.find_element_by_xpath("//td[@class='x-toolbar-left']//button[.='Искать']")

    @property
    def result_search_letter(self):
        return self.driver.find_element_by_css_selector("div > a.x-action-col-0.x-action-col-text")

    @property
    def url_activate_new_account(self):
        return self.driver.find_element_by_xpath("//a[.='Ссылка активации']")

    @property
    def search_field(self):
        self.driver.find_element_by_css_selector('input.search_field_cls').clear()
        return self.driver.find_element_by_css_selector('input.search_field_cls')

    @property
    def search_button(self):
        return self.driver.find_element_by_xpath('//button[.="Искать"]')

    @property
    def create_applic_btn(self):
        with allure.step("Зайти в подачу заявки"):
            return self.driver.find_element_by_css_selector('a.gridButtons_createApplic')

    @property
    def view_notice_button(self):
        with allure.step("Зайти в Просмотр извещения"):
            return self.driver.find_element_by_css_selector('a.x-action-col-9')

    @property
    def submitted_application_btn(self):
        with allure.step("Зайти в Поданные заявки"):
            return self.driver.find_element_by_css_selector("a.x-action-col-37")

    @property
    def open_applic_btn(self):
        with allure.step("Зайти во вскрытие заявок"):
            return self.driver.find_element_by_css_selector('a.gridButtons_openApplics')

    @property
    def review_applic_btn(self):
        with allure.step("Зайти в рассмотрение заявок"):
            return self.driver.find_element_by_css_selector('a.x-action-col-40')

    @property
    def summarizing_btn(self):
        with allure.step("Зайти в подведение итогов"):
            return self.driver.find_element_by_css_selector('a.gridButtons_reviewItog')

    @property
    def contracts_btn(self):
        with allure.step("Зайти в форму заключения договора"):
            return self.driver.find_element_by_css_selector("a.gridButtons_contractList")

    @property
    def trade_btn(self):
        with allure.step("Зайти на форму торгов"):
            return self.driver.find_element_by_css_selector('a.x-action-col-31')

    @property
    def settings(self):
        with allure.step("Настройки"):
            return self.button("Настройки")

    @property
    def about_organization(self):
        with allure.step("Сведения об организации"):
            return self.span_text("Сведения об организации")

    @property
    def view_change(self):
        with allure.step("Посмотреть / Изменить"):
            return self.span_text("Просмотреть\изменить")

    @property
    def organization(self):
        with allure.step("Организации"):
            return self.button("Организации")

    @property
    def search_organization(self):
        with allure.step("Поиск по организациям"):
            return self.span_text("Поиск по организациям")

    @property
    def app_for_registration(self):
        with allure.step("Заявки на регистрацию"):
            return self.span_text("Заявки на регистрацию")

    @property
    def contragent_name(self):
        with allure.step("Поле Наименование в поиске"):
            return self.driver.find_element_by_name("contragent_name")

    @property
    def inn(self):
        with allure.step("ИНН"):
            return self.driver.find_element_by_name("inn")

    @property
    def finance(self):
        with allure.step("Финансы"):
            return self.button("Финансы")

    @property
    def personal_account_status(self):
        with allure.step("Состояние лицевого счета"):
            return self.span_text("Состояние лицевого счета")

    @property
    def review_company_btn(self):
        with allure.step("Кнопка Рассмотреть"):
            return self.driver.find_element_by_xpath("//img[contains(@class,'x-action-col-0 x-action-col-icon')]")

    @Helper.wait_for_ajax()
    def view_personal_account(self):
        with allure.step("Переход в форму просмотра средств"):
            self.finance.click()
            self.personal_account_status.click()

    @Helper.wait_for_ajax()
    def search_for_accountant(self, value):
        with allure.step("Поиск по организациям от лица бухгалтера"):
            self.organization.click()
            self.search_organization.click()
            self.search_field.send_keys(value["inn"])
            self.search_button.click()

    @Helper.wait_for_ajax()
    def view_organization_data(self):
        with allure.step("Просмотр данных об организации"):
            self.settings.click()
            self.move_to(self.about_organization)
            self.view_change.click()

    @Helper.wait_for_ajax()
    def create_applic_button(self):
        self.create_applic_btn.click()

    @Helper.wait_for_ajax()
    def open_applic_button(self):
        self.open_applic_btn.click()

    @Helper.wait_for_ajax()
    def submitted_application_button(self):
        self.submitted_application_btn.click()

    @Helper.wait_for_ajax()
    def review_applic_button(self):
        self.review_applic_btn.click()

    @Helper.wait_for_ajax()
    def summarizing_button(self):
        self.summarizing_btn.click()

    @Helper.wait_for_ajax()
    def contracts_button(self):
        self.contracts_btn.click()

    @Helper.wait_for_ajax()
    def trade_button(self):
        self.trade_btn.click()

    @Helper.wait_for_ajax()
    def new_procedure(self):
        with allure.step("Переход на новую процедуру"):
            self.procedures_btn.click()
            self.span_text("Новая").click()

    @property
    def new_btn(self):
        with allure.step(f"Выбрать: Новая"):
            return self.driver.find_element_by_xpath(f"//span[.='Новая']")

    @Helper.wait_for_ajax()
    def admin_confirm_email_new_user(self, value):
        with allure.step("Выбрать администрирование"):
            self.administration_btn.click()
            self.move_to(self.journal_btn)
            with allure.step("Почтовые уведомления"):
                self.mail_notification.click()
                self.advanced_search.click()
                self.search_email_input.send_keys(value)
                self.not_sent_mails.click()
                self.search_advanced_btn.click()
                self.result_search_letter.click()
                self.url_activate_new_account.click()
                self.wait.until(lambda driver: self.span_text("Ваш аккаунт успешно активирован"))
                self.button("ОК").click()

    @Helper.wait_for_ajax()
    def new_procedure_ptype_gos(self):
        with allure.step('Переход на "Продажа и аренда государственного имущества"'):
            self.procedures_ptype_btn.click()
            self.move_to(self.new_btn)
            with allure.step("Продажа и аренда государственного имущества"):
                self.driver.find_element_by_xpath(f"//span[.='Продажа и аренда государственного имущества']").click()

    @Helper.wait_for_ajax()
    def new_procedure_ptype_com(self):
        with allure.step('Переход на "Продажа и аренда коммерческого имущества"'):
            self.procedures_ptype_btn.click()
            self.move_to(self.new_btn)
            with allure.step("Продажа и аренда коммерческого имущества"):
                self.driver.find_element_by_xpath(f"//span[.='Продажа и аренда коммерческого имущества']").click()

    @Helper.wait_for_ajax()
    def actual_procedure(self):
        self.procedures_btn.click()
        self.span_text("Актуальные процедуры").click()

    @Helper.wait_for_ajax()
    def find(self, name):
        self.search_field.send_keys(name)
        with allure.step(f"Поиск процедуры: {name}"):
            self.search_button.click()

    @Helper.wait_for_ajax()
    def my_apps(self):
        self.application_btn.click()
        self.span_text("Мои заявки").click()

    @property
    def application_btn(self):
        return self.button("Заявки на участие")

    @Helper.wait_for_ajax()
    def recall_applic_button(self):
        self.recall_applic_btn.click()

    @property
    def recall_applic_btn(self):
        with allure.step("Зайти в отзыв заявки"):
            return self.driver.find_element_by_css_selector('a.gridButtons_recallApplic')
