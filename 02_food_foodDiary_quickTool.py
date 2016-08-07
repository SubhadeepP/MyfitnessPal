class foodpage:
    def __init__(self,driver):
        self.driver = driver
          
    def click_Quick_add_calories(self):
        #click on Quick Tools
        self.driver.find_element_by_xpath("//td[@class='first alt']/div/a").click()
        #click on Quick Add Calories
        self.driver.find_element_by_xpath("//div[@id='quick_tools_0']/ul/li").click()
              
    