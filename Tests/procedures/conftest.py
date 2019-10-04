import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import IEDriverManager
from Report.video_record import VideoRecord


@pytest.fixture(scope="function")
def chrome_driver(request):
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    driver.get(f"https://{request.config.getoption('--url')}")
    video = VideoRecord().video(False)
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.JPG)
    if video:
        video.stdin.write("q".encode())
        video.stdin.close()
    driver.delete_all_cookies()
    driver.close()
    driver.quit()


@pytest.fixture(scope="function")
def firefox_driver(request):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    driver.get(f"https://{request.config.getoption('--url')}")
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.JPG)
    driver.close()
    driver.quit()


@pytest.fixture(scope="function")
def headless_driver(request):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--window-size=2000x2500")
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.implicitly_wait(30)
    request.cls.driver = driver
    driver.get(f"https://{request.config.getoption('--url')}")
    yield driver
    #    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.JPG)
    driver.close()
    driver.quit()


@pytest.fixture(scope="function")
def ie_driver(request):
    '''
    Обязательные настройки браузера:\n
     Свойства браузера - Безопасность - Установить чекбокс "Включить защищенный режим"\n
    для всех (четырех) зон.\n
     Дополнительно - Установить чекбокс "Включить 64-разрядные процессы для расширенного защищенного режима*"
    :param request:
    :return:
    '''
    driver = webdriver.Ie(executable_path=IEDriverManager().install())
    driver.maximize_window()
    driver.implicitly_wait(30)
    request.cls.driver = driver
    driver.get(f"https://{request.config.getoption('--url')}")
    yield driver
    allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.JPG)
    driver.delete_all_cookies()
    driver.close()
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--url", action="store", default="")