class loginDetails:
    
    def __init__(self,driver):
        self.driver = driver    
    
    def clickTologinButton1(self):
        #Click on the Login button on the first page of myfitness pal
        self.driver.find_element_by_xpath('//*[@id="navTop"]/li[7]/a').click()
        #//*[@id="navTop"]/li[7]/a
          
    def loginId_and_password(self,loginId,password):
        #After clicking on the the pop up comes with username and password
        login =self.driver.find_element_by_xpath("//input[@class='text' and @name='username']").send_keys(loginId)      
        Pwd = self.driver.find_element_by_xpath("//input[@class='text' and @name='password']").send_keys(password)  
        
    def clickTologinButton2(self):    
        #After clicking on the pop up click on the submit button
        self.driver.find_element_by_xpath("//li[@class='submit']/input").click()
          