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