from add_department.po.main_page import MAIN_PAGE


class Test_department:
    def setup(self):
        self.driver = MAIN_PAGE()

    def teardown(self):
        pass

    def test_add_department(self):
        result = self.driver.go_to_contact().click_add_go_to_NEM().click_sure().click_add()
        assert '测试' in result
