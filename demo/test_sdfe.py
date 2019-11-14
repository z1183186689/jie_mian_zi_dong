from time import sleep


def test_text(driver):
    driver.get("http://ui.yansl.com/#/message") #打开网址
    buttons=driver.find_element_by_xpath("//label[contains(text(),'自动关闭提示')]/..//button/span[text()='消息']")
    buttons.click()             #点击
    ml=driver.find_element_by_xpath("/html/body/div[2]/p")  #驱动查找元素路径
    text=ml.text
    print(text)                     #打印文本信息
    assert "这是一条消息" in text         #断言  in前面是否在后面里面
    sleep(2)


def test_source(driver):
    driver.get("http://ui.yansl.com")
    driver.find_element_by_xpath("//*[@id='app']/section/section/aside/ul/li[3]/div").click()
    sleep(2)
    driver.find_element_by_xpath("//*[@id='app']/section/section/aside/ul/li[3]/ul/li/ul/li[3]").click()
    source = driver.page_source#查看界面源代码
    print(source)
    assert "手工关闭提示" in source
    sleep(2)
    buttons = driver.find_element_by_xpath("//label[contains(text(),'自动关闭提示')]/..//button/span[text()='消息']")
    buttons.click()  # 点击
    ml = driver.find_element_by_xpath("/html/body/div[2]/p")  # 驱动查找元素路径
    text = ml.text
    print(text)  # 打印文本信息
    assert "这是一条消息" in text  # 断言  in前面是否在后面里面
    sleep(2)




