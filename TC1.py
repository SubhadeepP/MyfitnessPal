import unittest
from selenium import webdriver
from Common.DriverCreation import DriverStart
from Common.login import loginDetails
#from Pages.01_myHome_addFood import homepage    
from Pages.02_food_foodDiary_quickTool import foodpage
from Pages.03_food_quickAdd import quickFoodAdd
from Pages.myHome_Tabs_Validation import myhome_tab_validation


class Test(DriverStart,unittest.TestCase):

    def testName(self):
        
        userLogin = loginDetails(self.driver)
        userLogin.clickTologinButton1()
        userLogin.loginId_and_password('emailid', 'password')
        userLogin.clickTologinButton2()
        
        self.driver.implicitly_wait(15)
        
        myhomepage = homepage(self.driver)
        myhomepage.clickOnAddFood()
        
        
        clickFoodpage = foodpage(self.driver)
        clickFoodpage.click_Quick_add_calories()
        
        food_add = quickFoodAdd(self.driver)
        food_add.quick_add_clear()
        food_add.quick_add_Calories('2000')
        
        self.driver.implicitly_wait(15)
        self.driver.find_element_by_xpath(".//*[@id='ember1281']").click()
        
        
        myhomepage_tabs_validation = myhome_tab_validation(self.driver) 
        myhomepage_tabs_validation.hometabsAvailable()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()