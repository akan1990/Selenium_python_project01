import time
import pytest
from selenium import webdriver

class TestSample():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path='D:/Selenium_Section_1/Drivers/chromedriver.exe')
        driver.get('http://demowebshop.tricentis.com/login')
        driver.maximize_window()
        driver.implicitly_wait(10)
        yield
        driver.close()
        print('Test completed')

    def test_login(self, test_setup):
        driver.find_element_by_id('Email').send_keys('namasteduniya@company.com')
        driver.find_element_by_id('Password').send_keys('hello123')
        driver.find_element_by_xpath("//body/div[4]/div[1]/div[4]/div[2]/div[1]/div[2]/div[1]/div[2]/div[2]/form[1]/div[5]/input[1]").click()
        driver.find_element_by_link_text('Log out').click()
        x = driver.title
        assert x == 'Demo Web Shop'
        time.sleep(2)

    # def test_tearDown():
    #     driver.close()
    #     print('Test completed')
