from time import sleep

from selenium.webdriver.common.by import By


from Web.study03.selenium_wework_main1.page1.base_page import BasePage


class AddMember1(BasePage):

    #对添加成员页面元素进行操作
    def add_member(self):
        sleep(2)
        self.find(By.XPATH,'// *[ @ id = "username"]').send_keys('x6')
        sleep(2)
        self.find(By.XPATH,'//*[@id="memberAdd_acctid"]').send_keys('4446')
        sleep(2)
        self.find(By.XPATH,'//*[@id="memberAdd_phone"]').send_keys('11111111116')
        sleep(2)
        self.find(By.XPATH,'//*[@id="js_contacts75"]/div/div[2]/div/div[4]/div/form/div[3]/a[2]').click()
        sleep(3)
        return True

#使用右键检查定位元素
