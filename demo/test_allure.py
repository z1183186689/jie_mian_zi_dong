import allure


@allure.feature("一级分类")

@allure.story("二级分类")
@allure.title("标题")
@allure.issue("http://www.baidu.com",'bug')
@allure.testcase("http://www.baidu.com",'case')
def test_report(driver):
    url= "http://ui.yansl.com/#/checkbox"
    with allure.step("打开网址：{}".format(url)):pass
    driver.get(url)
    with allure.step("点击多选框: {}".format('//*[@id="form"]/form/div[1]/div/input[1]')):pass
    allure.attach(driver.get_screenshot_as_png(),'',allure.attachment_type.PNG)
    driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/input[1]').click()
    with allure.step("点击多选框：{}".format('//*[@id="form"]/form/div[1]/div/input[2]')):pass
    allure.attach(driver.get_screenshot_as_png(), '', allure.attachment_type.PNG)
    driver.find_element_by_xpath('//*[@id="form"]/form/div[1]/div/input[2]').click()

