from Base.initiateDriver import startBrowser,closeBrowser
from Library.ConfigReader import ElementsRead

def test_ValidateRegistration():
    driver=startBrowser()
    #driver.find_element('xpath',"//input[@name='firstname']").send_keys('Shyam')
    driver.find_element('name',ElementsRead('Registration','fname')).send_keys('Shyam')
    #driver.find_element('xpath',"//input[@name='lastname']").send_keys('Thapa')
    driver.find_element('name',ElementsRead('Registration','lname')).send_keys('Thapa')
    driver.find_element('name',ElementsRead('Registration','pwd')).send_keys('123@456')
    closeBrowser()
    