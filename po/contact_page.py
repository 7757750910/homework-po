import logging
from time import sleep

import allure
from selenium.webdriver.common.by import By

from add_department.po.basepage import Basepage
from add_department.po.new_department import NEW_DEPARTMENT


class CONTACT_PAGE(Basepage):
    _ADD = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
    _LINK = (By.LINK_TEXT, '添加部门')
    _NAME = (By.XPATH, '//*[@id="1688850949249783"]/ul')

    # 点击‘+’，进入新建部门
    def click_add_go_to_NEM(self):
        with allure.step('创建显性等待，直到‘+’可点击'):
            ele = (By.CSS_SELECTOR, '.member_colLeft_top_addBtn')
            # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(ele))
            self.wait_for_click(ele)
            logging.info('创建显性等待成功')
        with allure.step('点击‘+’'):
            # self.driver.find_element_by_css_selector('.member_colLeft_top_addBtn').click()
            self.find_click(*self._ADD)
            logging.info('点击‘+’')
        sleep(1)
        with allure.step('点击添加部门'):
            # self.driver.find_element_by_link_text('添加部门').click()
            self.find_click(*self._LINK)
            logging.info('点击添加部门')
        sleep(3)
        return NEW_DEPARTMENT(self.driver)

    # 输出页面信息，用于断言
    def click_add(self):
        sleep(3)

        with allure.step('找到页面中部门名称,并打印出'):
            # search = self.driver.find_element_by_xpath('//*[@id="1688850949249783"]/ul').text
            search = self.find(*self._NAME).text

            logging.info('成功找到页面中部门名称')

            logging.info('打印页面中部门名称')
        return search
