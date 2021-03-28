from common.base import Base
from selenium.webdriver.common.action_chains import ActionChains

class AddJiGou(Base):
    loc_机构管理 = ('xpath',"//span[contains(text(),'机构管理')]")
    loc_机构列表 = ('css','ul:nth-child(2) > li.el-menu-item.is-active')
    #loc_机构列表 = ('xpath', "//span[contains(text(),'机构管理')]/../*[@text='机构列表']")
    loc_我要添加下级机构 = ('xpath',"//*[@class='el-button el-button--info el-button--medium']")
    loc_选择上级机构 = ('xpath','//div[2]/div/div/div/div/div/input')
    loc_大脚超市 = ('css','div.el-select-dropdown__wrap.el-scrollbar__wrap:nth-child(1) > ul.el-scrollbar__view.el-select-dropdown__list')    #[4][0]
    
    def click_Management(self):
        '''点击机构管理'''
        self.click(self.loc_机构管理)

    def click_list(self):
        '''点击机构列表'''
        self.move_to_element(self.loc_机构列表)
        self.click(self.loc_机构列表)


    def click_add_jigou(self):
        '''点击我要添加下级机构'''
        self.click(self.loc_我要添加下级机构)




if __name__ == '__main__':
    from selenium import webdriver
    from pages.login_page import LoginPage
    driver = webdriver.Chrome()
    driver.maximize_window()
    web = LoginPage(driver)
    web.login()
    res = web.is_login_success()
    print("登陆结果：%s"%res)

    #添加下级机构
    add = AddJiGou(driver)
    add.click_Management()
    print('1')
    add.click_list()
    print('2')
    add.click_add_jigou()
    print('3')
