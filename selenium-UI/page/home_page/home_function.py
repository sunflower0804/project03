from time import sleep

from selenium.webdriver.common.by import By

from Web.UI.base_page.basepage import BasePage

#1.2首页功能验证
class Home_Function(BasePage):
    #1.2.1自动提醒成员使用开关按钮功能验证
    def click_button(self):
        self.find(By.XPATH,'//*[@id="_hmt_click"]/div[2]/div[1]/div[5]/div[1]/span/span').click() #默认关闭，点击后开启，并出现闪现提示信息:"已开启自动邀请"
        sleep(2)
        text = self.find(By.XPATH,'//*[@id="js_tips"]').text
        sleep(2)
        self.find(By.XPATH, '//*[@id="_hmt_click"]/div[2]/div[1]/div[5]/div[1]/span/span').click()  #还原
        return text

    def download_App(self):
        self.find(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[2]/div/div[2]/div[1]/a/div[4]').click()
        return True
