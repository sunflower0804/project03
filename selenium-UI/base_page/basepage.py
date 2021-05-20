from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    _driver = None  #类变量，需要在类函数之前进行赋值
    _base_url = ''
    #__init__:父类的构造方法，子类执行之前首先会去调用执行父类的构造方法
    def __init__(self, driver: WebDriver = None): #: WebDriver = None
        #这里如果不对参数进行初始化会报错：TypeError: __init__() missing 1 required positional argument: 'driver'
        #定义页面基础类时，初始化webdiver，传参数的时候没有对参数driver赋默认None值，即一个默认参数，导致页面报错如下：
        #传人默认参数，在调用self.main=Main()时，就可以不传入参数了(或者直接在调用时传入默认参数初始值self.main=Main(WebDriver = None))
        #且不指定浏览器驱动类型时，后面调用时定位元素会出问题
        if driver is None:   #如果外面没有对driver进行传值（即第一次调用），那么就对driver进行初始化
            options = Options() #使用 selenium 时，我们可能需要对 chrome 做一些特殊的设置，以完成我们期望的浏览器行为，比如阻止图片加载，阻止JavaScript执行 等动作。这些需要 selenium的 ChromeOptions 来帮助我们完成
            options.debugger_address = '127.0.0.1:9500'  #开启浏览器调试模式：cmd命令窗口输入： chrome  --remote-debugging-port=端口1（随便取），回车
            self._driver = webdriver.Chrome(options=options)
            sleep(2)
            #加入隐式等待时间
            # #弊端：全局生效，但只要找到元素不管有没有完全加载就继续下一步，这样会造成操作失败
            #self._driver.implicitly_wait(10)
            #解决办法:使用显示等待

        else:
            self._driver = driver  #后面每次有方法调用self._driver时，都是初始化之后的driver

        if self._base_url != '':
            self._driver.get(self._base_url)

    #将find_element进行封装
    def find(self, by, locator):
        return self._driver.find_element(by, locator)

    #将find_elements进行封装
    def finds(self, by, locator):
        return self._driver.find_elements(by, locator)

    #将显示等待进行封装
    def wait_for_click(self,locator,time = 10):
        WebDriverWait(self._driver, time).until(expected_conditions.element_to_be_clickable(locator))



