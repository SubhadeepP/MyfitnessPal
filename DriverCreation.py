
import unittest
from selenium import webdriver

class DriverStart(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('https://www.myfitnesspal.com/')
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

    #def tearDown(self):
    #    self.driver.quit()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()