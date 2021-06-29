import logging
from time import sleep

import allure
from selenium.webdriver.common.by import By

from add_department.po.basepage import Basepage


class NEW_DEPARTMENT(Basepage):
    _NAME = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input', '测试')
    _DEPART = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a')
    _DEPARTMENT = (By.XPATH,
                   '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/div/div/ul//*[@id="1688850949249783_anchor"]')
    _SURE = (By.XPATH, '//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]')

    # 点击确定，返回通讯录页面
    def click_sure(self):
        # 局部导入
        from add_department.po.contact_page import CONTACT_PAGE
        # 输入部门名称
        with allure.step('输入部门名称'):
            # #self.driver.find_element_by_xpath(
            #     '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[1]/input').send_keys(
            #     '测试1')
            self.find_sends(*self._NAME)
            logging.info('输入部门名称')
        # 选择所属部门
        with allure.step('选择所属部门'):
            # self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/a').click()

            self.find_click(*self._DEPART)

            # self.driver.find_element_by_xpath(
            #     '//*[@id="__dialog__MNDialog__"]/div/div[2]/div/form/div[3]/div/div/ul//*[@id="1688850949249783_anchor"]').click()

            self.find_click(*self._DEPARTMENT)
            logging.info('选择所属部门')
        # 点击确定按钮
        with allure.step('点击确定按钮'):
            # self.driver.find_element_by_xpath('//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]').click()

            self.find_click(*self._SURE)
            logging.info('点击确定按钮')
        sleep(3)
        return CONTACT_PAGE(self.driver)
