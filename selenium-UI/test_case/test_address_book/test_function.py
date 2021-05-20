
from Web.UI.base_page.main import Main


#class Test_Address_Book_Function(BasePage):  #报错：PytestCollectionWarning: cannot collect test class 'Test_Address_Book_Function' because it has a __init__ constructor (from: test_function.py)
#报错原因：pytest不能包含__init__构造的方法
class Test_Address_Book_Function:
    def setup(self):
        self.main = Main(driver=None)

    # 1.1首页功能验证测试用例
    #测试点1：检查首页自动提醒成员使用开关按钮功能
    def test_address_book_search(self):
        print(self.main.goto_address_book_search().address_book_search())


