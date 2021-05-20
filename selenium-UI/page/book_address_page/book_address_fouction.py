
from time import sleep

from selenium.webdriver.common.by import By

from Web.UI.base_page.basepage import BasePage

# 2.2通讯录模块首页页面功能验证

class Book_Address_Function(BasePage):
    # 2.2.1搜索框功能验证
    def address_book_search(self):
        sleep(2)
        return self.find(By.XPATH, '//*[@id="1688850919007961"]/div/div[3]/div[1]/div[2]/div[1]/div[1]').text


