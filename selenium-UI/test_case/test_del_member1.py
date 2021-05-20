from Web.study03.selenium_wework_main.page.main import Main


class TestDelMember:
    def setup(self):
        self.main = Main()

    def test_add_member(self):
        self.main.goto_main_del_member().del_members()