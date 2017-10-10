from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from getpass import getpass

def perform():
    usr = raw_input('Enter your E-Mail ID: ')
    pwd = getpass('Enter Password: ')

    driver = webdriver.Firefox(executable_path = '/media/vivek/Coding Stuffs/Python_Projects/geckodriver')
    respond =  "Network Connection not found"
    #driver.manage().window().maximize();
    try:
        driver.get('https://www.facebook.com/')

        usr_box = driver.find_element_by_name('email')
        pwd_box = driver.find_element_by_name('pass')

        usr_box.send_keys(usr)
        pwd_box.send_keys(pwd)

        login = driver.find_element_by_xpath('//*[@id="u_0_6"]')
        login.submit()

    except Exception:
        print "Sorry ERROR Encountered! Try Again..."
        exit(1)

if __name__ == '__main__':
    perform()

"""
if login.submit():
    print "Successfully Logged In"
else:
    print "Autentication Failed"
"""

"""
except selenium.common.exceptions.WebDriverException:
    print "Network Connection Problem"


except NoSuchWindowsException:
    print "Can't locate Login ID" """
