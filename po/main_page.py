import logging

import allure
from selenium.webdriver.common.by import By

from add_department.po.basepage import Basepage
from add_department.po.contact_page import CONTACT_PAGE


class MAIN_PAGE(Basepage):
    _CON = (By.XPATH, '//*[@id="menu_contacts"]/span')
    # 点击通讯录，进入通讯录界面
    def go_to_contact(self):
        with allure.step('点击通讯录，进入通讯录页面'):
            # self.driver.find_element_by_xpath('//*[@id="menu_contacts"]/span').click()
            self.find_click(*self._CON)
            logging.info('进入通讯录页面')
            return CONTACT_PAGE(self.driver)
