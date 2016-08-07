class myhome_tab_validation:
      
    def __init__(self,driver):
        self.driver = driver
        
    def hometabsAvailable(self):
        #check home is present
        
        print (self.driver.find_element_by_xpath(".//*[@id='ember1356']").text) 