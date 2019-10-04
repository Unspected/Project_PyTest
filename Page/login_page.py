import allure

from Page.base import BaseProcedures
from Page.helper import Helper


class LoginPage(BaseProcedures):

    def logout(self):
        with allure.step("Выход"):
            url = self.driver.current_url.split("/#")
            self.driver.get(url[0] + '/#auth/logout')
            self.driver.delete_all_cookies()

    @property
    def register_button(self):
        return self.button('Регистрация')

    @property
    def enter_username(self):
        return self.driver.find_element_by_name("username")

    @property
    def enter_password(self):
        return self.driver.find_element_by_name("pass")

    @Helper.wait_for_ajax()
    def login(self, value):
        with allure.step(f"Площадка: {(self.driver.current_url.split('/#'))[0]}"):
            self.enter_username.clear()
            self.enter_username.send_keys(value['login'])
        with allure.step(f"Логин:{value['login']}"):
            self.enter_password.clear()
            self.enter_password.send_keys(value['password'])
        with allure.step(f"Пароль:{value['password']}"):
            self.button("Вход").click()

    @Helper.wait_for_ajax()
    def registration(self):
        with allure.step("Переход на форму регистрации"):
            self.register_button.click()