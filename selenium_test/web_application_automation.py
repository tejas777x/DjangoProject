from selenium import webdriver   # import selenium webdriver
from selenium.webdriver.support.select import Select
driver = webdriver.Chrome('E:\python\chromedriver')  # chrome driver path
driver.set_page_load_timeout(30)
driver.implicitly_wait(90)
driver.set_script_timeout(30)
driver.get("http://127.0.0.1:8000/") # url of the website
driver.find_element_by_name("q").click()  # function to click on registration block
driver.find_element_by_name("username").send_keys("goo")  # function to enter username in the registration form
driver.find_element_by_name("password").send_keys("maxin123")  # function to enter password in the registration form
driver.find_element_by_name("email").send_keys("maxin@gmail.com")  # function to enter email in the registration form
driver.find_element_by_name("mobile_no").send_keys("237232382")  # function to enter mobile_no in the registration form
driver.find_element_by_name("address").send_keys("chock")  # function to enter address in the registration form
driver.find_element_by_name("g").click()  # function to click on register button
driver.find_element_by_name("p").click()  # function to click on login block
driver.find_element_by_name("username").send_keys("goo")  # function to enter username in the login form
driver.find_element_by_name("password").send_keys("maxin123")  # function to enter password in the login form
driver.find_element_by_name("u").click()  # function to click on login button
driver.find_element_by_name("y").click()  # function to got to database.html
obj = Select(driver.find_element_by_name("select1"))  # function to click on first drop down box
obj.select_by_index(2)  # function to select option
obj1 = Select(driver.find_element_by_name("select2"))   # function to click on first drop down box
obj1.select_by_value("9")  # function to select option
button = driver.find_element_by_xpath('//button[@id="45"]')  # function to find button
button.click()  # function to select button
button_1= driver.find_element_by_xpath('//button[@id="SURAJ"]')   # function to find button
button_1.click()  # function to select button

