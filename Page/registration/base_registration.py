import allure
from Page.base import BaseProcedures
from Page.helper import Helper
from Page.login_page import LoginPage
import time

from Page.main_page import MainPage
from Values.members import Members


class BaseRegistration(BaseProcedures):
    def __init__(self, driver):
        super().__init__(driver)
        self.main = MainPage(self.driver)
        self.role = None
        self.type_company = None

    def registration_page(self, value):
        LoginPage(self.driver).registration()
        self.choose_resident_status(value)
        self.fill_user_info(value)
        self.choose_role_in_system(value["role"])
        self.fill_organizator_info(value)
        LoginPage(self.driver).logout()
        LoginPage(self.driver).login(Members().ADMIN_ETP)
        MainPage(self.driver).admin_confirm_email_new_user(value["user_mail"])
        self.button('Закрыть').click()
        LoginPage(self.driver).logout()

    @Helper.wait_for_ajax()
    def choose_role_in_system(self, role):
        """Для СНГ резидента только значения 1 и 2"""
        role_list = {
            1: "Участник закупки",
            2: "Заказчик",
            3: "Организатор"
        }
        with allure.step("Желаемая роль в системе: " + role_list[role]):
            self.driver.find_element_by_xpath(
                f"//input[contains(@class,' x-form-radio x-form-field')][@value={role}]").click()
            self.role = role
            return role

    def fill_organizator_info(self, *args):
        pass

    @Helper.wait_for_ajax()
    def choose_resident_status(self, value):
        """
        :param country: 1 - Резидент РФ
                       2 -Резидент стран СНГ
                       3 - Резидент иностранных государств
        :return:
        """
        with allure.step(f"Выбор резидентского статуса {str(value['resident'])}"):
            self.driver.find_element_by_xpath(
                f"//input[@name='resident_status'][@value={str(value['resident'])}]").click()
            self.next_button.click()

    @property
    def next_button(self):
        with allure.step("Кнопка далее"):
            return self.button("Далее -->")

    @property
    def username(self):
        self.driver.find_element_by_name("username").clear()
        return self.driver.find_element_by_name("username")

    @property
    def password(self):
        self.driver.find_element_by_name("pass").clear()
        return self.driver.find_element_by_name("pass")

    @property
    def password_repeat(self):
        self.driver.find_element_by_name("confpass").clear()
        return self.driver.find_element_by_name("confpass")

    @property
    def secret_word(self):
        self.driver.find_element_by_name("secret_phraze").clear()
        return self.driver.find_element_by_name("secret_phraze")

    @property
    def email_adress(self):
        self.driver.find_element_by_name("user_email").clear()
        return self.driver.find_element_by_name("user_email")

    @property
    def last_name(self):
        self.driver.find_element_by_name("last_name").clear()
        return self.driver.find_element_by_name("last_name")

    @property
    def first_name(self):
        self.driver.find_element_by_name("first_name").clear()
        return self.driver.find_element_by_name("first_name")

    @property
    def middle_name(self):
        self.driver.find_element_by_name("middle_name").clear()
        return self.driver.find_element_by_name("middle_name")

    @property
    def user_job(self):
        self.driver.find_element_by_name("user_job").clear()
        return self.driver.find_element_by_name("user_job")

    @property
    def user_phone_country_code(self):
        # Установить 1 цифру например 7
        with allure.step("Телефон код страны"):
            self.driver.find_element_by_name("user_phone[cntr_code]").clear()
            return self.driver.find_element_by_name("user_phone[cntr_code]")

    @property
    def user_phone_city_code(self):
        with allure.step("Телефон код города"):
            self.driver.find_element_by_name("user_phone[city_code]").clear()
            return self.driver.find_element_by_name("user_phone[city_code]")

    @property
    def user_phone_number(self):
        with allure.step("Телефон номер"):
            self.driver.find_element_by_name("user_phone[number]").clear()
            return self.driver.find_element_by_name("user_phone[number]")

    @property
    def next_button_userform(self):
        with allure.step("Кнопка Далее в форме Данные о пользователе"):
            time.sleep(0.5)
            return self.driver.find_element_by_xpath(
                "//table[@class='x-btn button-bolder x-btn-noicon']//button[contains(@class,'x-btn-text')][contains(text(),'-->')]")

    def fill_phone_number(self, number=79035557788):
        with allure.step(f"Телефон пользователя: {number}"):
            tel = str(number)
            self.user_phone_country_code.send_keys(tel[:2])
            self.user_phone_city_code.send_keys(tel[2:5])
            self.user_phone_number.send_keys(tel[4:])

    @Helper.wait_for_ajax()
    def fill_user_info(self, value):
        with allure.step("Заполнение данных пользователя"):
            with allure.step(f"Имя пользователя: {value['login']}"):
                self.username.send_keys(value["login"])
            with allure.step(f'Пароль и повтор пароля: {value["password"]}'):
                self.password.send_keys(value['password'])
                self.password_repeat.send_keys(value["password"])
            with allure.step("Секретное слово Secret"):
                self.secret_word.send_keys("Secret")
            with allure.step(f"Электронная почта пользователя: {value['user_mail']}"):
                self.email_adress.send_keys(value["user_mail"])
            with allure.step(f"Имя пользователя: {value['first_name_user']}"):
                self.first_name.send_keys(value["first_name_user"])
            with allure.step(f"Фамилия пользователя: {value['last_name_user']}"):
                self.last_name.send_keys(value["last_name_user"])
            with allure.step(f"Должность и подразделение: {value['job_user']}"):
                self.user_job.send_keys(value["job_user"])
            with allure.step(f"Телефон пользователя: {value['user_phone']}"):
                self.fill_phone_number(value["user_phone"])
            self.next_button_userform.click()