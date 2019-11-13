from time import sleep

import pytest
from selenium import webdriver
def test_prorse(driver):
    #打开浏览器
    driver=webdriver.Chrome('../chrome_driver_v77/chromedriver.exe')
    sleep(1)
    #driver.close()
    #调整浏览器窗口大小
    #driver.maximize_window()
    #打开网址
    driver.get("http://www.baidu.com")
    sleep(1)
    #打开京东
    driver.get("http://jd.com")
    sleep(1)
    #前进
    driver.forward()
    sleep(1)
    #后退
    driver.back()
    sleep(1)
    #刷新
    driver.refresh()
    sleep(1)

    driver.quit()