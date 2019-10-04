from time import perf_counter, sleep
import allure
from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementClickInterceptedException, StaleElementReferenceException, \
    ElementNotInteractableException, JavascriptException


class Helper:

    def wait_for_ajax(step=0.5, time_out=10):
        def wrapper(func):
            def sub_wrapper(self, *args, **kwargs):
                time_out_ajax = perf_counter()
                while time_out > perf_counter() - time_out_ajax:
                    try:
                        func(self, *args, **kwargs)
                        self.wait.until(lambda driver: self.driver.execute_script(
                            'return !Ext.Ajax.isLoading() && Ext.query(".x-mask-loading").length==0;'))
                        break
                    except (
                            ElementClickInterceptedException, StaleElementReferenceException,
                            ElementNotInteractableException, JavascriptException):
                        # with allure.step("ElementClickInterceptedException"):
                        #     allure.attach(self.driver.get_screenshot_as_png(), name="ElementClickInterceptedException",
                        #                   attachment_type=AttachmentType.JPG)
                        #     print("ElementClickInterceptedException")
                        sleep(step)
                # print(f"ajax:", func.__name__, perf_counter() - time_out_ajax)

            return sub_wrapper

        return wrapper