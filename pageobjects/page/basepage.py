#新增一个basepage文件
#base_page:完成一个类，对通用代码的一个引入，对__init__做一个封装，被其他需要__init__的PO类来调用
#让所有的子类继承BasePage
from selenium import webdriver


class BasePage:
    def __init__(self,driver=None):
        #index页面始终是从外面传的driver,按照PO原则，不想让这些内容污染case
        if driver == None:
            self.driver = webdriver.Chrome()
            #self.driver.get("https://work.weixin.qq.com/")
            #对访问地址进行自定义操作,让PO类可以自定义地址  变量名称前加_ 表示的是私有化变量
            self.driver.get(self._base_url)

            self.driver.implicitly_wait(3)
        else:
            self.driver=driver
