from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Basepage:
    def __init__(self, driver_base: WebDriver = None):
        if driver_base is None:
            opt = webdriver.ChromeOptions()
            opt.debugger_address = "127.0.0.1:9222"
            self.driver = webdriver.Chrome(options=opt)
            self.driver.implicitly_wait(10)
            self.driver.get("https://work.weixin.qq.com/wework_admin/frame")

        else:
            self.driver = driver_base

    def find_click(self, by, locator):
        ele = self.driver.find_element(by, locator).click()
        return ele

    def find(self, by, locator):
        ele = self.driver.find_element(by, locator)
        return ele

    def find_sends(self, by, locator, xxx):
        ele = self.driver.find_element(by, locator).send_keys(xxx)
        return ele
    def wait_for_click(self, locator, timeout=10):
        # 元素注解 : WebElement
        element: WebElement = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(locator))
