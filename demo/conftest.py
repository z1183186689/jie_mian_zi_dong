from time import sleep

import pytest
from selenium import webdriver
@pytest.fixture(scope="session")
def driver():
    #打开浏览器
    driver=webdriver.Chrome('../chrome_driver_v77/chromedriver.exe')
    sleep(1)
    #driver.close()
    #调整浏览器窗口大小
    #driver.maximize_window()
    yield driver
    driver.quit()