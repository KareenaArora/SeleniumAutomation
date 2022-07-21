from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path = "C:\\Users\\kareena.a\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/")

# Mouse Operation like hover over some text, right click, double click, etc
act = ActionChains(driver)
# Not specifying where to click ... So click/left click where ever the mouse is
# act.click().perform()
# Pressing right click
# act.context_click().perform()

# Now locating the element where to click/left click
# act.click(driver.find_element("xpath","//a[@title='Contact Us']")).perform()

# Right click
# act.context_click(driver.find_element("xpath","//a[@title='Contact Us']")).perform()

# Double Click
#act.double_click().perform()
#act.double_click(driver.find_element("xpath","//a[@title='Contact Us']")).perform()

# Move to element
act.move_to_element(driver.find_element("xpath","//span[contains(text(),'TUTORIAL')]")).perform()

# Also we can perform drag and drop
