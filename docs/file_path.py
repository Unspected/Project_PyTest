import os
from os.path import join

import allure
from colorama import Back, Fore


class Files:

    def __init__(self):
        self.dir_path = os.path.dirname(__file__)

    def get_file(self, file_name):
        try:
            file = join(self.dir_path, file_name)
            if os.path.exists(file):
                return file
            else:
                raise
        except:
            with allure.step(f"Файл '{file_name}' не найден!"):
                print(Fore.RED + f"Файл '{file_name}' не найден!")
