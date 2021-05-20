from time import sleep

from selenium.webdriver.common.by import By

from Web.study03.selenium_wework_main1.page1.base_page import BasePage

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

class Members1(BasePage):

    def add_members(self):
        #sleep(2)
        # 使用显示等待判断元素是否满足等待条件
        locator = self.find(By.XPATH,'//*[@id="js_contacts82"]/div/div[2]/div/div[2]/div[3]/div[1]/a[1]')
        self.wait_for_click(self,locator,5)
        locator.click()
        sleep(2)
        self.find(By.XPATH,'// *[@id="username"]').send_keys('xx7')
        sleep(2)
        self.find(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys('4446')
        sleep(2)
        self.find(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys('11111111118')
        sleep(2)
        self.find(By.CSS_SELECTOR,'#js_contacts78 > div > div.member_colRight > div > div:nth-child(4) > div > form > div:nth-child(3) > a.qui_btn.ww_btn.js_btn_save').click()
        sleep(3)
        return True

    def get_members(self):
        elements = self.find(By.XPATH,'//*[@id="member_list"]/tr[4]/td[2]')
        for i in elements:
            return elements


    def del_members(self):
        sleep(2)
        #勾选要删除的成员
        self.find(By.XPATH,'//*[@id="member_list"]/tr[3]/td[1]/input').click()
        sleep(3)
        # #点击删除
        self.find(By.XPATH,'//*[@id="js_contacts69"]/div/div[2]/div/div[2]/div[3]/div[1]/a[3]').click()
        sleep(2)
        # #此时出现弹框，点击确认
        self.driver.switch_to.alert.accept()   #获取当前弹框，并点击确认
        #sleep(2)//*[@id="__dialog__MNDialog__"]/div/div[3]/a[1]
        #报错：未生效：selenium.common.exceptions.NoAlertPresentException: Message: no such alert
        return True

