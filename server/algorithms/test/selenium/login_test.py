from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

print('IMPORTANT: Make sure you have Chromedriver.exe installed to match the same version as chromium!')

port = int(sys.argv[2])
email = sys.argv[3]
password = sys.argv[4]
if sys.argv[1].lower() == 'chrome':
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=options)
elif sys.argv[1].lower() == 'firefox':
    driver = webdriver.Firefox()
elif sys.argv[1].lower() == 'opera':
    driver = webdriver.Opera()

print('Beginning the LOGIN TEST at http:\\localhost:{} with the {} browser.'.format(port, sys.argv[1]))
print('Using the following credentials:\nEmail: {}\nPassword: {}'.format(email, password))

try:
    driver.get("http://localhost:{}/".format(port))
    assert(driver.title == 'React App')
    print('The current page title is: {}'.format(driver.title))
    print('>>> Test 1 Passed!')
    form = driver.find_element_by_id("Loginemail")
    form.send_keys(email)
    form = driver.find_element_by_id("Loginpassword")
    form.send_keys(password)
    print('The email ({}) and password ({}) were successfully input.'.format(email, password))
    print('>>> Test 2 Passed!')
    form.send_keys(Keys.RETURN)
    alerttext = Alert(driver)
    assert alerttext.text == 'Email:  {}\nPassword: {}'.format(email, password)
    print('An alert has contained the following text:\n{}'.format(alerttext.text))
    print('>>> Test 3 Passed!')
    print('>>> All Tests Passed!\nThe login test is now complete!')

except:
    print('The test has failed...')
