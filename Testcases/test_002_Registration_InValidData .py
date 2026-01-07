from Base.initiateDriver import startBrowser,closeBrowser
import time

def test_Validate_Invalid_data_Registration():
    driver=startBrowser()
    driver.find_element('xpath',"//input[@name='firstname']").send_keys('1234@')
    driver.find_element('xpath',"//input[@name='lastname']").send_keys('8950')
    closeBrowser()
time.sleep(30)  