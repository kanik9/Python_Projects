from selenium import webdriver
from getpass import getpass

usr = raw_input("Enter Username: ")
pwd = getpass("Enter Password: ")

driver = webdriver.Firefox(executable_path = '/media/vivek/Coding Stuffs/Python_Projects/geckodriver')
driver.get('http://172.50.1.1:8090/httpclient.html')

usr_box = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[2]/td/input')
#aleternative is to use find_element_by_name = username
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_xpath('/html/body/form/div[1]/div[2]/div[2]/table/tbody/tr[4]/td/input')
pwd_box.send_keys(pwd)

login = driver.find_element_by_id('logincaption')
login.submit()

driver.close()
