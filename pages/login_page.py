from common.base import Base
from common.config import test_host

login_url = test_host+'/#/login/'

class LoginPage(Base):
    loc_1 = ('name','brhId')         #机构号
    loc_2 = ('name', 'account')        #用户名
    loc_3 = ('name', 'password')        #密码
    loc_4 = ('xpath', "//body/div[@id='app']/div[1]/div[2]/div[1]/div[1]/div[1]/div[2]/div[4]/button[1]")    #立即登陆按钮
    loc5 = ('xpath',"//span[contains(text(),'欢迎光临')]")    #判断元素

    def input_jigou(self,jigou):
        '''输入机构号'''
        self.send(self.loc_1,jigou)

    def input_user(self,username):
        '''输入账号'''
        self.send(self.loc_2,username)

    def input_psw(self,psw):
        '''输入密码'''
        self.send(self.loc_3,psw)

    def click_button(self):
        '''点击登陆按钮'''
        self.click(self.loc_4)

    def login(self,jigou='0229043000',username='xzh1',psw='Aa123456!'):
        '''登陆'''
        self.driver.get(login_url)
        self.input_jigou(jigou)
        self.input_user(username)
        self.input_psw(psw)
        self.click_button()

    def is_login_success(self):
        '''判断是否登陆成功，返回bool值'''
        text = self.get_text(self.loc5)
        print('登陆完成后，获取页面文本元素 %s'%text)
        return text == '欢迎光临'

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
    assert result
    driver.quit()