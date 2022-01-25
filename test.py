import unittest
import os
from appium import webdriver
from time import sleep

PATH = lambda p: os.path.abspath(
    os.path.dirname(__file__), p)


class test_leroy(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['deviceName'] = 'LG K50'
        # desired_caps['app'] = PATH('leroymerlin.apk')
        desired_caps['udid'] = 'LMX5209PCAB6S8R8BA'
        desired_caps['appPackage'] = 'com.mec.leroy'
        desired_caps['appActivity'] = 'com.mec.leroy.MainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()


    def testApp1(self):
        driver = self.driver
        button = driver.find_element_by_xpath(
                    "//android.widget.TextView[@bounds='[91,54][182,128]']")
        button.click()
        sleep(3)
        search = driver.find_element_by_xpath("//*[@text='Szukaj']")
        search.send_keys("beton architektoniczny")
        driver.find_element_by_xpath(
            "//android.widget.TextView[@bounds='[28,153][95,222]']").click()
        sleep(3)




if __name__ == 'main':
    suite = unittest.TestLoader().loadTestsFromTestCase(test_leroy)
    unittest.TextTestRunner(verbosity=2).run(suite)
