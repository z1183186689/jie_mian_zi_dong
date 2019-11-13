from time import sleep

from selenium.webdriver import ActionChains


def test_input(driver):
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)

    input =driver.find_element_by_xpath("//input[@name='t1']")
    input.clear()
    input.send_keys("我是你大爷。很牛的我")
    sleep(5)

def test_radio(driver):
    driver.get("http://ui.yansl.com/#/radio")
    sleep(1)

    radio =driver.find_element_by_xpath("//input[@name='sex'][2]")
    #点击
    radio.click()
    sleep(2)

def test_checkbox(driver):
    driver.get("http://ui.yansl.com/#/checkbox")
    sleep(2)

    checkbox=driver.find_element_by_xpath("//label[text()='多选框2']/..//span[1]")
    attribute = checkbox.get_attribute("class")
    if not attribute=='el-checkbox is-checked':
        checkbox.click()
        sleep(5)
    checkbox = driver.find_element_by_xpath("//label[text()='多选框2']/..//span[1]")
    attribute = checkbox.get_attribute("class")
    if  attribute == 'el-checkbox is-checked':
        checkbox.click()
        sleep(5)
def test_select(driver):                                        #
    driver.get("http://ui.yansl.com/#/select")
    sleep(2)

    select =driver.find_element_by_xpath("//label[text()='下拉框2']/../div/div")
    #点击
    select.click()
    sleep(2)
    option = driver.find_element_by_xpath("(//span[text()='双皮奶'])[last()]")
    actions = ActionChains(driver)
    actions.move_to_element(option).perform()
    sleep(2)
    option.click()
    sleep(2)

def test_slider(driver):
    driver.get("http://ui.yansl.com/#/slider")
    sleep(2)

    slider = driver.find_element_by_xpath("//label[text()='竖向选择']/../div/div/div/div/div")
    sleep(2)
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(slider,0,-200).perform()
    sleep(2)