from Web.UI.base_page.main import Main


class TestSearchUI:
    def setup(self):
        self.main = Main(driver=None)

    # 1.1首页功能验证测试用例
    #测试点1：检查首页自动提醒成员使用开关按钮功能
    def test_click_button(self):
        assert "已开启自动邀请" == self.main.goto_main_click_button().click_button()

    # 测试点2:下载桌面端
    # 点击立即下载，直接链接下载地址并下载(#如何测试下载文件类型)
    def test_download_App(self):
        assert True == self.main.goto_main_download_App().download_App()