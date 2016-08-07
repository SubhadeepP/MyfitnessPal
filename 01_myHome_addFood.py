class homepage:
      
    def __init__(self,driver):
        self.driver = driver
      
    def clickOnAddFood(self):
        #click on Add Food in the home page
        self.driver.find_element_by_xpath(".//*[@id='ember1655']").click()
        
