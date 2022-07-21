from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def test_registration():
    path = Service("C:\\Users\\kareena.a\\Downloads\\chromedriver_win32\\chromedriver.exe")
    driver = Chrome(service=path)
    driver.get("http://www.theTestingWorld.com/testings")
    driver.maximize_window()
    driver.find_element("name","fld_username").send_keys("helloworld")
    driver.find_element("name","fld_email").send_keys("helloworld@gmail.com")
    driver.find_element("name","fld_password").send_keys("abcd123")
    driver.find_element("name","fld_cpassword").send_keys("abcd123")


































