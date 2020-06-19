import excel_function  # import the excel_function.py file
from selenium import webdriver  # import selenium webdriver
driver=webdriver.Chrome('E:\python\chromedriver') # path of chrome
driver.get("https://www.netflix.com/in/Login?nextpage=https%3A%2F%2Fwww.netflix.com%2Fbrowse") # url of the website
driver.maximize_window()  # to maximise the window
path= "data1.xlsx" # path of the excel file

# get count of the rows in the excel sheet
rows=excel_function.getRowCount(path, "Sheet3")


print("len", rows)
for r in range(2, rows+1):
    try:

        password = excel_function.readData(path, "Sheet3", r, 2)
        email_id = excel_function.readData(path, "Sheet3", r, 1)

        driver.find_element_by_name("userLoginId").send_keys(email_id)
        driver.find_element_by_name("password").send_keys(password)
        driwer.find_element_by_name("")
        if driver.title == "Netflix":
            print("test is passed")
            result = excel_function.writeData(path, "Sheet3", r, 3, "test passed")
        driver.implicitly_wait(2)



    except Exception as e:
        print(e)

