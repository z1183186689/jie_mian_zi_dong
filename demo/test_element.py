from time import sleep

import autoit
from selenium.webdriver import ActionChains#导入类
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC  # 定义了变量EC表示expected_conditions




def test_input(driver):#纯输入框，输入内容
    driver.get("http://ui.yansl.com/#/input")
    sleep(2)

    input =driver.find_element_by_xpath("//input[@name='t1']")
    input.clear()
    input.send_keys("我是你大爷。很牛的我")
    sleep(5)

def test_radio(driver):#
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

def test_time(driver):
    driver.get("http://ui.yansl.com/#/dateTime")
    sleep(1)

    t1=driver.find_element_by_xpath("//label[text()='固定时间']/../div/div/input")
    t1.clear()
    t1.send_keys("14:19:25")
    sleep(2)


def test_file(driver):#上传文件，图片，等等
    driver.get("http://ui.yansl.com/#/upload")
    sleep(1)

    file = driver.find_element_by_xpath("//label[text()='原始上传']/..//input")
    file.clear()
    file.send_keys("C:\\Users\\guoya\\Pictures\\qwer_20191028123217.png")
    sleep(2)


def test_file2(driver):#上传文件，图片，等等
    driver.get("http://ui.yansl.com/#/upload")
    sleep(1)

    file=driver.find_element_by_xpath("//label[text()='缩略图列表']/..//span")
    file.click()
    sleep(2)
    autoit.win_wait("打开", 10)
    sleep(1)
    # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    autoit.control_set_text("打开", "Edit1", "C:\\Users\\guoya\\Pictures\\qwer_20191028123217.png")
    sleep(2)
    autoit.control_click("打开", "Button1")
    sleep(2)

def test_alert(driver):
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)


    button = driver.find_element_by_xpath("/html/body/table/tbody/tr[6]/td[2]/input")
    button.click()
    sleep(2)
    alert=driver.switch_to.alert
    alert.send_keys("sadasf")
    alert.accept()
    sleep(2)



def test_windows(driver):   #定义方法名test开头(调用公用包方法)
    driver.get("http://192.168.1.128:8082/xuepl/demo.html")
    sleep(2)

    dang_dang = driver.find_element_by_link_text("当当")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dang_dang).key_up(Keys.CONTROL).perform()
    sleep(2)
    jd = driver.find_element_by_link_text("京东")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(jd).key_up(Keys.CONTROL).perform()
    sleep(2)
    dn = driver.find_element_by_partial_link_text("度娘")
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(dn).key_up(Keys.CONTROL).perform()
    sleep(2)


    handles = driver.window_handles         # 获取所有窗口的句柄
    for h in handles:           #循环 h变量

        driver.switch_to.window(h)      # 根据窗口句柄，切换窗口
        sleep(2)
        if driver.title.__contains__("京东"):      #判断是否在京东页面
            break                                        #关闭


def test_from(driver):
    driver.get("http://192.168.1.128:8082/xuepl1/frame/main.html")
    sleep(2)

    frame=driver.find_element_by_xpath('/html/frameset/frameset/frame[1]')
    driver.switch_to.frame(frame)
    sleep(2)
    driver.find_element_by_partial_link_text('京东').click()
    sleep(2)


    driver.switch_to.parent_frame()     #退出当前ifame
    sleep(2)
    iframe=driver.find_element_by_xpath('/html/frameset/frameset/frame[2]') #进入frome
    driver.switch_to.frame(iframe)  #切换frame
    sleep(2)                        #响应时间
    inpu=driver.find_element_by_xpath('//*[@id="key"]')     #定位输入框
    inpu.clear()              #清空
    inpu.send_keys('手机')                                #输入内容
    sleep(2)

def test_wher(driver):
    driver.get("http://ui.yansl.com/#/loading")                #打开网址
    bt=driver.find_element_by_xpath("//button/span[contains(text(),'指令方式')]")   #驱动查找元素路径
    bt.click()
    WebDriverWait(driver, 5, 0.5).until(
        EC.presence_of_element_located((By.XPATH, '//tbody/tr[2]/td[2]/div[text()="王小虎"]'))
    )   #
    bg=driver.find_element_by_xpath("//tbody/tr[2]/td[2]/div[text()='王小虎']")#驱动查找元素路径
    print(bg.text)      #打印文本
    sleep(2)