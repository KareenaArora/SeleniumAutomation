from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

path = "C:\\Users\\kareena.a\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")
driver.maximize_window()

# Fetching Page title
print(driver.title)

# Fetching URL
print(driver.current_url)

# Fetching the page source (html code)
print("----------------------------------------------")
# print(driver.page_source)

# Fetch Text written on Element
print(driver.find_element(By.CLASS_NAME,"displayPopup").text)

# Fetch attribute value
print(driver.find_element("xpath","//input[@type='submit']").get_attribute("value"))

# Fetch selected option from dropdown
obj = Select(driver.find_element("name","sex"))
obj.select_by_value("2")
# print(obj.all_selected_options)
# above statement is used in list
print(obj.first_selected_option.text)

# Fetch all available options
print("All available options are :- ")
for op in obj.options:
    print(op.text)





