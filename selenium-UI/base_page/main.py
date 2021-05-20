from time import sleep

from basepage import BasePage


class Main(BasePage):
    #进入首页（扫码登录的步骤通过basepage模块中复用已登录过的企业微信完成）
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'

    #1.首页模块
    #1.1页面信息检查
    def goto_main_searchUI(self):
        sleep(2)
        return Home_Search_UI(self._driver)

    #1.2首页功能验证
    #1.2.1自动提醒成员使用开关按钮
    def goto_main_click_button(self):
        sleep(2)
        return Home_Function(self._driver)

    #1.2.2下载桌面端
    #点击立即下载，直接链接下载地址并下载
    def goto_main_download_App(self):
        sleep(2)
        return Home_Function(self._driver)


    #1.3首页其它模块功能验证（这里只需验证跳转是否正常，跳转过后直接return到跳转后的页面对应功能的方法
    #1.3.1探索企业微信栏（首次验证，验证通过后此栏不存在）
    #1.3.1.2完善通讯录
    #点击导入成员，出现弹窗：
    #（1）选择批量导入，点击确认后跳转进入通讯录模块的批量导入导出功能的文件导入页面
    #（2）选择通过腾讯企业邮箱导入，点击确认后跳转进入通讯录模块的批量导入导出功能的导入腾讯企业邮箱通讯录页面
    #（3）选择手动添加成员，点击确认后跳转进入通讯录模块的添加成员页面
    def goto_main_import_member(self):
        sleep(2)
        pass  #点击导入成员，出现弹窗：
        #选择判断
            #（1）
            #（2）
            #（3）


    #1.3.1.3探索企业应用
    #点击前往查看，出现弹窗，点击确认后跳转进入应用管理模块首页
    def goto_main_search_WeApplication(self):
        sleep(2)
        pass   #点击前往查看，出现弹窗，点击确认
        return Application_management(self._driver)


    #1.3.2常用入口功能验证
    #2.3.2.1添加成员
    #点击添加成员跳转进入通讯录模块的添加成员页面
    def goto_main_add_member(self):
        sleep(2)
        self.find(By.XPATH,'//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        sleep(2)
        return AddMember1(self._driver)  #self._driver参数首先会传到BasePage中（因为BasePage是它的父类），然后将它的driver赋值给self._driver进行使用




    # 点击进入通讯录再进入添加成员页面
    def goto_main_add_members(self):
        sleep(2)
        self.find(By.XPATH,'//*[@id="menu_contacts"]/span').click()
        return Members1(self._driver)

    #点击将进入通讯录页面再删除成员
    def goto_main_del_member(self):
        sleep(2)
        self.find(By.XPATH,'//*[@id="menu_contacts"]/span').click()  #点击进入通讯录
        return Members1(self._driver)


    #2.通讯录模块Address_Book
    def address_bookUI(self):
        #return self.find(By.CSS_SELECTOR,'css=#menu_contacts > .frame_nav_item_title')
        return self.find(By.XPATH, '//*[@id="menu_contacts"]/span').click()  # 进入通讯录模块
    #2.1通讯录模块首页页面信息检查
    #无单独不变的文本信息


    #2.2通讯录模块首页页面功能验证
    #2.2.1搜索框功能验证
    def goto_address_book_search(self):
        self.address_bookUI()
        sleep(2)
        #self.find(By.XPATH, '//*[@id="memberSearchInput"]').send_keys('科比')   #先点击再输入
        #self.find(By.XPATH,'//*[@id="js_contacts52"]/div/div[1]/div/div[1]/span/span[1]').click()
        self.find(By.ID, "memberSearchInput").click()
        self.find(By.ID, "memberSearchInput").send_keys("科")
        sleep(2)
        return Book_Address_Function(self._driver)







    #2.3模块功能验证
    #2.1组织架构模块Organization
    #2.1.1添加子部门
    #点击进入通讯录再进入组织架构





    #2.2标签模块