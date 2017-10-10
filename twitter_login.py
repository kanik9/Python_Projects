from selenium import webdriver
from getpass import getpass

#binary = FirefoxBinary('/Applications/Firefox.app/Contents/MacOS/firefox-bin')

usr = raw_input("Enter your Username: ")
pwd = getpass("Enter password: ")

driver = webdriver.Firefox(executable_path = '/media/vivek/Coding Stuffs/Python_Projects/geckodriver')
driver.get('https://twitter.com/login')

usr_box = driver.find_element_by_class_name('js-username-field')
usr_box.send_keys(usr)

pwd_box = driver.find_element_by_class_name('js-password-field')
pwd_box.send_keys(pwd)

login = driver.find_element_by_css_selector('button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium')
login.submit()
