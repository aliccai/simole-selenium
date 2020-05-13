# coding:utf-8
import unittest
from selenium import webdriver
from time import sleep


class TestBaidu(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        cls.url = 'https://www.baidu.com/'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_search_key_sel(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id("kw").send_keys("selenium")
        self.driver.find_element_by_id("su").click()

        sleep(2)

        title = self.driver.title
        self.assertEqual(title, "selenium_百度搜索")

    def test_search_key_app(self):
        self.driver.get(self.url)
        self.driver.find_element_by_id("kw").send_keys("appium")
        self.driver.find_element_by_id("su").click()

        sleep(2)

        title = self.driver.title
        self.assertEqual(title, "appium_百度搜索")


if __name__ == '__main__':
    unittest.main()
