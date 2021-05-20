
from time import sleep



from Web.UI.base_page.main import Main


class TestSearchUI:
    def setup(self):
        self.main = Main(driver=None)

    # 1.1首页页面信息检查测试用例
    #测试点1：检查首页是否存在对应文字
    def test_search_text(self):
        assert "自动提醒成员使用" == self.main.goto_main_searchUI().search_text()

    #测试点2：检查将鼠标移动到二维码上，在出现的悬浮窗上点击“下载企业微信二维码”链接后是否生效（生效会提示：“复制成功”）
    def test_copy_code(self):
        assert "复制成功" == self.main.goto_main_searchUI().test_moveto_code()




