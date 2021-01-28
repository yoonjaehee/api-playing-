import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome("C://chromedriver")

driver.get("http://www.megastudy.net/teacher_v2/t_promotion/202101_pr/0118_megabori/main.asp")
driver.execute_script("fncShowLogin()")
driver.implicitly_wait(3)
time.sleep(1)
driver.find_element_by_id("loginidly").send_keys("id")
driver.implicitly_wait(3)
time.sleep(1)
driver.find_element_by_id("loginpwly").send_keys("password")
driver.implicitly_wait(3)
time.sleep(1)
driver.execute_script("goLoginly()")
driver.implicitly_wait(3)
time.sleep(1)
while(1):
    try:
        driver.execute_script("fncAppJoin('2021-01-24')")
        driver.switch_to.alert.accept()
    except:
        pass
##using pypy
