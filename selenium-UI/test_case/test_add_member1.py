from time import sleep

from Web.study03.selenium_wework_main1.page1.main1 import Main


class TestAddMember:
    def setup(self):
        self.main = Main(driver=None)

    def test_add_member(self):
        #self.main.goto_main_add_member().add_member()

        self.main.goto_main_add_members().add_members()
        #sleep(2)
        #assert 'xx7' in self.main.goto_main_add_member().get_members()