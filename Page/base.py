import allure
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from Values.members import Members
from docs.file_path import Files


class BaseProcedures:

    def __init__(self, driver):
        self.driver = driver
        self.member = Members()
        self.wait = WebDriverWait(driver, 30)

    def attach_file_base(self, block_name, file_name, file='document.docx'):
        '''
        Добавление файла в поля с двойными полями, указания имени файла и ссылку на файл
        :param block_name: Имя блока где содержатся поля
        :param file_name: Наименование файла в виде строки, для поля указания имени файла
        :param file: Полное наименование файла из docs (По умолчанию 'document.docx')
        '''
        with allure.step(f"Добавить файл: '{file_name}' ({file}) в блок: {block_name}"):
            self.driver.find_element_by_xpath(
                f'//span[contains(text(), "{block_name}")]/../..//input[contains(@class, "fileDescrCt")]').send_keys(
                file_name)
            self.driver.find_element_by_css_selector('input.x-form-file:not([disabled])').send_keys(
                self.get_file(file))
            self.wait.until(lambda driver: self.driver.find_element_by_link_text(file_name))

    def attach_file_accreditation(self, block_name, file_name, file='Registration.docx'):
        """Для аккредитации контрагентов"""
        with allure.step(f"Добавить файл: '{file_name}' ({file}) в блок: {block_name}"):
            self.driver.find_element_by_xpath(
                f'//span[contains(text(),"{block_name}")]/../../../../..//input[contains(@class, " fileDescrCt")]').send_keys(
                file_name)
            self.driver.find_element_by_xpath(
                f'//span[contains(text(),"{block_name}")]/following::input[@type="file"][not(@disabled)]').send_keys(
                self.get_file(file))
            self.wait.until(lambda driver: self.driver.find_element_by_link_text(file_name))

    def get_file(self, file_name):
        '''
        Получение файла для полей без указания имени файла\nk
        Примеры:\n self.get_file("units_applic.xls")\n
        self.driver.find_element_by_name("path").send_keys(self.get_file("units_applic.xls"))\n
        :param file_name: Полное наименование файла из docs
        :return: Ссылку на файл
        '''
        return Files().get_file(file_name)

    def span_text(self, text):
        with allure.step(f"Выбрать: {text}"):
            return self.driver.find_element_by_xpath(f"//span[.='{text}']")

    def button(self, button_name):
        with allure.step(f"Нажать: {button_name}"):
            return self.driver.find_element_by_xpath(f"//button[.='{button_name}']")

    def move_to(self, element):
        '''Навести на элемент страницы \n
        loc = self.driver.find_element_by_xpath("...") \n
        self.move_to(loc)'''
        ActionChains(self.driver).move_to_element(element).perform()

    def label(self, label_name):
        with allure.step(f"Текст(label): {label_name}"):
            return self.driver.find_element_by_xpath(f"//label[.='{label_name}']")

    def wait_signature_text(self):
        '''
        Ожидание и получение подписываемого текста
        :return: Массив подписываемого текста, разделенного запятыми по переводу строки
        '''
        self.wait.until(lambda driver: self.driver.find_element_by_name("signature_text").get_attribute("value"))
        return self.driver.find_element_by_name("signature_text").get_attribute("value").split('\n')

    def wait_supplier_signature_text(self):
        '''
                Ожидание и получение подписываемого текста
                :return: Массив подписываемого текста, разделенного запятыми по переводу строки
                '''
        self.wait.until(
            lambda driver: self.driver.find_element_by_name("supplier_signature_text").get_attribute("value"))
        return self.driver.find_element_by_name("supplier_signature_text").get_attribute("value").split('\n')

    def drop_cron_procedures(self):
        with allure.step(f'Запуск крона процедур '):
            url = self.driver.current_url.split("/#")
            self.driver.get(url[0] + "/cron/procedures")
            try:
                self.driver.implicitly_wait(5)
                self.driver.find_element_by_xpath("//p[contains(text(),'успешно')]")
            except NoSuchElementException:
                try:
                    self.driver.implicitly_wait(1)
                    self.driver.find_element_by_xpath("//h2[contains(text(),'Копия данного скрипта уже запущена')]")
                except NoSuchElementException:
                    raise NoSuchElementException
            self.driver.get(url[0])

    def wait_ok_message(self):
        self.wait.until(lambda driver: self.driver.find_element_by_xpath(f"//span[.='Успешно']"))

    def sign_index_text(self, array: list, text: str):
        '''
        Ищет значение в массиве и получает список индексов и значений
        :return: список с кортежем (индекс index_list, значение string_list) по заданному совпадающему значению
        '''
        index_list = [index for index, string in enumerate(array) if string == f'{text}'][0]
        string_list = [string for index, string in enumerate(array) if string == f'{text}'][0]
        return index_list, string_list

    def get_part_list_text(self, array: list, text: str, num: int):
        '''
        Вырезает диапазон значений из массива
        :param array: Любой список значений list
        :param text: Начальное значение списка ("От")
        :param num: Количество последующих значений списка, включая значение "От"
        :return: Список значений вида ['знач1', 'знач2',...'знач3']
        '''
        index_list, string_list = self.sign_index_text(array, text)
        arr_sign_string = []
        for n in range(num):
            arr_sign_string.append(array[index_list + n])
        return arr_sign_string

    def assertion(self, actual, expected, text_allure='Проверка данных'):
        '''
        Метод проверки данных, для упрощения написания в коде
        :param actual: Ожидаемое значение
        :param expected: Фактическое значение
        :param text_allure: Текст проверки для отчета
        '''
        with allure.step(f"{text_allure}"):
            assert actual == expected, f'\nОжидаемое: {actual}\nФактическое: {expected}'

    def checkbox(self, checkbox, need_select: bool):
        '''
        Установить или снять чекбокс вне зависимости от его текущего состояния
        :param checkbox: Элемент чекбокса со страницы (Пример: self.driver.find_element_by_name("lock_ip"))
        :param need_select: True - Установить, False - Не устанавливать
        '''
        if need_select and checkbox.is_selected():
            pass
        elif need_select and not checkbox.is_selected():
            with allure.step("Установить чекбокс"):
                checkbox.click()
                self.checkbox(checkbox, need_select)
        elif checkbox.is_selected():
            with allure.step("Снять чекбокс"):
                checkbox.click()
                self.checkbox(checkbox, need_select)

    def check_exists_css_selector(self, selector):
        try:
            self.driver.implicitly_wait(0.5)
            self.driver.find_element_by_css_selector(selector)
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(30)
        return True

    def check_exists_xpath(self, xpath):
        try:
            self.driver.implicitly_wait(0.5)
            self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException:
            return False
        finally:
            self.driver.implicitly_wait(30)
        return True
