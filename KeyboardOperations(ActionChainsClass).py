from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time

path = "C:\\Users\\kareena.a\\Downloads\\chromedriver_win32\\chromedriver.exe"
driver = Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")


driver.find_element("name","fld_username").send_keys("Hello")

# Now you want to press tab (keyboard operation)
# For that import Action Chain Class

act = ActionChains(driver)
# Now our keyboard keys are divided into two
# One is normal keys which includes characters/alphabets
# Rest of the keys like tab, caps lock, ctrl, page up, etc are special keys
# So we need to import keys class

# act.send_keys(Keys.TAB).perform()

# Now performing Ctrl+A operation
act.key_down(Keys.CONTROL).send_keys('a').perform()
time.sleep(5)
act.send_keys(Keys.DELETE).perform()