from common.base import Base
from common.config import test_host

login_url = test_host+'/#/login/'

class LoginPage(Base):
    loc_1 = ('name','brhId')         #机构号
    loc_2 = ('name', 'account')        #用户名
    loc_3 = ('name', 'password')        #密码
    loc_4 = ('xpath', "//body/div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/button[1]")    #立即登陆按钮
    loc5 = ('xpath',"//span[contains(text(),'欢迎光临')]")    #判断元素

    def login(self,jigou='0229043000',username='xzh1',password='Aa123456!'):
        '''登陆'''
        self.driver.get(login_url)
        self.send(self.loc_1,jigou)
        self.send(self.loc_2,username)
        self.send(self.loc_3,password)
        self.click(self.loc_4)

    def is_login_success(self):
        '''判断是否登陆成功，返回bool值'''

        result = self.is_element_exist(self.loc_5)
        return result

if __name__ == '__main__':
    from selenium import webdriver
    import time
    driver = webdriver.Chrome()
    web = LoginPage(driver)
    driver.get('https://plat.vpos.xin/#/login/')
    web.login('0229043000','xzh1','Aa123456!')
    #判断登陆
    result = web.is_login_success()
    print(result)
    driver.quit()