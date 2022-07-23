import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from multiprocessing import Process
def crawling():
    driver = webdriver.Chrome("C://chromedriver")
    driver.get("https://kiusugang.kiu.ac.kr/sookang/login_kiujs_lp.jsp")
    driver.find_element_by_name("userID").send_keys("")
    driver.implicitly_wait(3)
    time.sleep(1)
    driver.find_element_by_name("userPWD").send_keys("")
    driver.implicitly_wait(3)
    time.sleep(1)
    driver.execute_script("arguments[0].click();",driver.find_element_by_xpath('//input[@type="image"][@src="/sookang/images/btn_login.gif"]'))
    driver.implicitly_wait(3)
    time.sleep(1)
    driver.switch_to.frame("fBody")
    driver.find_element_by_xpath("/html/body/div[3]/table[2]/tbody/tr/td[2]/table[1]/tbody/tr[1]/td[2]/input").send_keys("S050160")
    driver.find_element_by_id("id_aType02").send_keys("02")
    driver.find_element_by_id("btnShowSbjList").click()
    driver.switch_to.frame("sbjPro_01")
    time.sleep(1)
    driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/button").click()
    while(1):
        try:
            time.sleep(0.2)
            driver.switch_to.alert.accept()
            time.sleep(0.2)
            driver.switch_to.alert.accept()
            driver.find_element_by_xpath("/html/body/div/div[3]/div[3]/div/table/tbody/tr[2]/td[1]/button").send_keys(Keys.ENTER)
        except:
            pass
    
if __name__=='__main__':
    p1 = Process(target=crawling) #함수 1을 위한 프로세스
    p1.start()
    
    
