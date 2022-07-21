from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
'''Need to import 'Select' module from selenium for dropdown/list test case'''
from selenium.webdriver.support.select import Select
'''
NOTE :- 
Need a chromedriver (bridge) to connect my test case with browser
So we installed chrome driver and set ts path in path variable and used that while creating object of the browser
'''

'''setting path for chrome driver'''
path = "C:\\Users\\kareena.a\\Downloads\\chromedriver_win32\\chromedriver.exe"
'''creating browser object to open the browser'''
driver = Chrome(executable_path=path)
'''Entering URL'''
driver.get("http://www.theTestingWorld.com/testings")
'''Maximizing the browser'''
driver.maximize_window()
'''Enter data in textbox'''
driver.find_element("name","fld_username").send_keys("helloworld")
driver.find_element("name","fld_email").send_keys("helloworld@gmail.com")
driver.find_element("name","fld_password").send_keys("abcd123")
driver.find_element("name","fld_cpassword").send_keys("abcd123")
'''trying to enter the username again'''
'''It will append'''
driver.find_element("name","fld_username").send_keys("helloworld123")
'''Now task is clear the existing text in the textbox and then enter '''
driver.find_element("name","fld_username").clear()
driver.find_element("name","fld_username").send_keys("abcd123")
'''Working on radio button'''
driver.find_element("xpath","//input[@value='home']").click()
'''driver.find_element("xpath","//input[@value='office']").click()'''
'''Working on checkbox'''
driver.find_element("name","terms").click()
'''Click on Sign Up button'''
driver.find_element("xpath","//input[@type='submit']").click()
'''Working on links - similar to buttons/checkbox/radiobutton'''
driver.find_element(By.LINK_TEXT,"Read Detail").click()
time.sleep(5)
driver.find_element(By.CLASS_NAME,"close").click()

'''
dropdown -> can select only one value
list -> can select multiple values
'''

# Working on dropdown
obj = Select(driver.find_element("name","sex"))
# select value by index
# going by index -> it is numeric
# obj.select_by_index(2)

# select by value
# inspect the HTML ... for each option we will be having some value
# going by value -> it is string
# obj.select_by_value("2")

# select value by text
obj.select_by_visible_text("Female")
time.sleep(5)

''' DESELECT doesn't work with dropdown 
obj.deselect_by_visible_text("Female")
'''

''' We can DESELECT the values in list
obj.deselect_all()
obj.deselect_by_index()
obj.select_by_value()
obj.deselect_by_visible_text()
'''

driver.close()

































