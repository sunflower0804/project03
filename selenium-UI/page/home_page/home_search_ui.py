from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium import webdriver

from Web.UI.base_page.basepage import BasePage


class Home_Search_UI(BasePage):

    #对首页页面内容进行检查
    #1.1页面信息检查
    #检查页面文本信息：“自动提醒成员使用”
    def search_text(self):
        sleep(2)
        return self.find(By.XPATH,'//*[@id="_hmt_click"]/div[2]/div[1]/div[5]/div[2]/div[1]').text

    #将鼠标移动到某个元素上：“下载企业微信二维码”
    def test_moveto_code(self):
        sleep(2)
        #定位到二维码图标
        code = self.find(By.XPATH,'//*[@id="_hmt_click"]/div[2]/div[1]/div[6]/div[1]/span')
        action = ActionChains(self._driver)
        action.move_to_element(code)
        action.perform() #鼠标悬停后才会出现的元素，然后找到该元素，正常定位即可
        self.find(By.XPATH,'//*[@id="copyDownload"]').click()  #悬停出现的文本内容“复制下载链接”的超链接,并点击
        return self.find(By.XPATH,'//*[@id="js_tips"]').text        #点击后出现闪现的提示信息，定位方法如下：
        #操作步骤：
        #因为闪退弹窗速度比较快，需要按如下步骤操作：
        #1)在打开的浏览器中按F12 ，选择Sources；
        #2)操作触发弹窗步骤；
        #3) 鼠标按下暂停图标（pause） 或快捷键（Ctrl +\），这样弹窗就暂停了，不会闪退了（这里如果动作慢也可能定位不到，就需要重复步骤2）和3）了）;
        #4)再选Elements,鼠标选中弹窗内容就可以定位了。
        sleep(3)

