import excel_function  # import the excel_function.py file
from selenium import webdriver  # import selenium webdriver
driver=webdriver.Chrome('E:\python\chromedriver') # path of chrome
driver.get("http://127.0.0.1:8000/") # url of the website
driver.maximize_window()  # to maximise the window
path= "data1.xlsx" # path of the excel file

# get count of the rows in the excel sheet
rows=excel_function.getRowCount(path, "Sheet1")


print("len", rows)
for r in range(2, rows+1):
    try:
        username = excel_function.readData(path, "Sheet1", r, 1)  # read username from the excel sheet
        password = excel_function.readData(path, "Sheet1", r, 2)  # read password from the excel sheet
        email_id = excel_function.readData(path, "Sheet1", r, 3)  # read email_id from the excel sheet
        mobile_no = excel_function.readData(path, "Sheet1", r, 4)  # read mobile_no from the excel sheet
        address = excel_function.readData(path, "Sheet1", r, 5)  # read address from the excel sheet

        driver.find_element_by_name("q").click()   # function to click on registration block
        driver.find_element_by_name("username").send_keys(username)  # function to enter username in the registration form
        driver.find_element_by_name("password").send_keys(password)  # function to enter password in the registration form
        driver.find_element_by_name("email").send_keys(email_id)   # function to enter email in the registration form
        driver.find_element_by_name("mobile_no").send_keys(mobile_no)   # function to enter mobile_no in the registration form
        driver.find_element_by_name("address").send_keys(address)   # function to enter address in the registration form
        driver.find_element_by_name("g").click()   # function to click on register button
        driver.implicitly_wait(2)


    except Exception as e:
        print(e)

