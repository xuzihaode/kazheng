from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select         #下拉选择框
from selenium.webdriver.common.action_chains import ActionChains     #模拟鼠标
from selenium.common.exceptions import NoSuchElementException     #判断页面上某个元素是否存在
from selenium.common.exceptions import NoSuchFrameException    #iframe
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import TimeoutException

'''封装selenium基本操作'''

class LocatorTypeError(Exception):
    pass

class ElementNotFound(Exception):
    pass

class Base():
    '''selenium二次封装'''

    def __init__(self,driver:webdriver.Chrome, timeout=10, t=0.5):
        self.driver = driver
        self.timeout = timeout
        self.t = t

    def find(self,locator):
        '''定位到元素，返回元素对象，没定位到，Timeout异常'''
        if not isinstance(locator,tuple):            #判断一个对象是否是一个已知的类型
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")      #手动设置异常
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" %(locator[0], locator[1]))
            try:
                ele = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_element_located(locator))
            except TimeoutException as msg:
                raise ElementNotFound("定位元素超时，请检查你的定位方式")
            return ele

    def finds(self,locator):
        '''复数定位，返回elements对象'''
        if not isinstance(locator,tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元组类型：loc = ('id','value1')")
        else:
            print("正在定位元素信息：定位方式->%s,value值->%s" % (locator[0], locator[1]))
            eles = WebDriverWait(self.driver,self.timeout,self.t).until(EC.presence_of_all_elements_located(locator))
            return eles

    def send(self,locator,text=''):
        '''发送文本'''
        ele = self.find(locator)
        if ele.is_displayed():       #判断元素是否显示
            ele.send_keys(text)
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法输入，解决办法：定位唯一元素，或先让元素可见，或者用js输入")

    def click(self,locator):
        '''点击元素'''
        ele = self.find(locator)
        if ele.is_displayed():
            ele.click()
        else:
            raise ElementNotVisibleException("元素不可见或者不唯一无法点击，解决办法：定位唯一元素，或先让元素可见，或者用js点击")

    def clear(self,locator):
        '''清空输入框文本'''
        ele = self.find(locator)
        ele.clear(locator)

    def is_selected(self,locator):
        '''判断元素是否被选中，返回bool值'''
        ele = self.find(locator)
        r = ele.is_selected()
        return r

    def is_element_exist(self,locator):
        '''判断元素是否存在，返回bool值'''
        try:
            self.find(locator)
            return True
        except:
            return False

    def is_title(self,title=''):
        '''判断当前页面的title是否精确等于预期,返回bool值'''
        try:
            result = WebDriverWait(self.driver,self.timeout,self.t).until(EC.title_is(title))
            return result
        except:
            raise False

    def is_title_contains(self,title=''):
        '''判断当前页面的title是否包含预期字符串,返回bool值'''
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, text=''):
        """检查指定的元素中是否存在相应的文本,返回bool值"""  #https://blog.csdn.net/tiekun888/article/details/106923011/
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, value=''):
        """返回bool值，value为空字符串，返回False"""  #判断元素中的value属性是否包含了预期的字符串
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except:
            return False

    def is_alert(self, timeout=3):
        '''判断弹出框是否存在，返回bool值'''
        try:
            result = WebDriverWait(self.driver, timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def get_title(self):
        """获取title"""
        return self.driver.title

    def get_text(self, locator):
        """获取文本"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            t = self.find(locator).text
            return t
        except:
            print("获取text失败，返回''")
            return ""

    def get_attribute(self, locator, name):
        """获取属性"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        try:
            element = self.find(locator)
            return element.get_attribute(name)
        except:
            print("获取%s属性失败，返回''" %name)
            return ''

    def js_focus_element(self, locator):
        """聚焦元素"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        target = self.find(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """滚动到顶部"""
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        """滚动到底部"""
        js = "window.scrollTo(%s, document.body.scrollHeight)"%x
        self.driver.execute_script(js)

    def select_by_index(self, locator, index=0):
        """定位下拉框中的选项，通过索引，index是索引第几个，从0开始，默认第一个"""  #https://huilansame.github.io/huilansame.github.io/archivers/drop-down-select
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_index(index)

    def select_by_value(self, locator, value):
        """通过value属性"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        element = self.find(locator)
        Select(element).select_by_value(value)

    def select_by_text(self, locator, text):
        """通过文本值定位"""
        element = self.find(locator)
        Select(element).select_by_visible_text(text)

    def switch_iframe(self, id_index_locator):
        """切换iframe"""
        try:
            if isinstance(id_index_locator, int):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, str):
                self.driver.switch_to.frame(id_index_locator)
            elif isinstance(id_index_locator, tuple):
                ele = self.find(id_index_locator)
                self.driver.switch_to.frame(ele)
        except:
            print("iframe切换异常")

    def switch_handle(self, window_name):
        '''切换窗口'''
        self.driver.switch_to.window(window_name)

    def switch_alert(self):
        '''返回bool值'''
        r = self.is_alert()
        if not r:
            print("alert不存在")
        else:
            return r

    def move_to_element(self, locator):
        """鼠标悬停操作"""
        if not isinstance(locator, tuple):
            raise LocatorTypeError("参数类型错误，locator必须是元祖类型：loc = ('id','value1')")
        ele = self.find(locator)
        ActionChains(self.driver).move_to_element(ele).perform()


if __name__ == '__main__':
    driver = webdriver.Chrome()
    web = Base(driver) #浏览器实例化
    driver.get('https://www.baidu.com')
    loc_1 = ('id','kw')
    web.send(loc_1,'hello world')

    driver.close()
