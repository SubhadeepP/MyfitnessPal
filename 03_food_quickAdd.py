class quickFoodAdd:
    def __init__(self,driver):
        self.driver = driver
        
    def quick_add_clear(self):
        #check calories as a text value is present and clear the value 
        print (self.driver.find_element_by_xpath("//span[@class='description energy']").text)
        self.driver.find_element_by_xpath("//div[@class='right col']/span/input").clear()
        
    def quick_add_Calories(self,inputCalorie):  
        #input the calories and submit the "Add to Diary"
         
        self.driver.find_element_by_xpath("//div[@class='right col']/span/input").send_keys(inputCalorie)
        #self.driver.find_element_by_xpath("//div[@class='quick-add-macros']/div/div/div/div/a/a").click()
        #self.driver.find_element_by_partial_link_text("Add to Diary").click()
        self.driver.find_element_by_xpath(".//*[@id='ember1392']/div/div[4]/a[2]").click()
           
        