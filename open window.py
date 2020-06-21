from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

webdriver = webdriver.Chrome()  # type: WebDriver

#Assert.assertEquals(expectedUrl,  driver.getCurrentUrl());

#website = websiteDesired

#print ("enter website: ")
#input (website)
#print (website)



webdriver.get("http://www.google.com")
webdriver.find_element(By.NAME, "q").click()
webdriver.find_element(By.NAME, "q").send_keys("wikipedia")
webdriver.find_element(By.NAME, "btnK").click()

#trying to find a clickable first link, by copying JS and XPath from CSS
#document.querySelector('#rso > div:nth-child(1) > h2')
#//*[@id="cnt"]/div[9] Xpath
#document.querySelector('#rso > div:nth-child(1) > div > link')
#webdriver.find_element(By.CSS_SELECTOR, "#rso > div:nth-child(1) > h2").click()
#webdriver.find_element(By.CSS_SELECTOR, "#rso > div:nth-child(1) > div > link").click()
#document.querySelector('#rso > div:nth-child(1) > div > div > div.r > a')

#found a clickable element!
webdriver.find_element(By.CSS_SELECTOR, "#rso > div:nth-child(1) > div > div > div.r > a").click()

#verify at wiki
#webdriver.get.current_url();
#error webdriver.getCurrentUrl();
#AttributeError: 'WebDriver' object has no attribute 'getCurrentUrl'
#Assert.assertEquals("www.wikipedia.org",  webdriver.current_url());

# Getting current URL 
get_title = webdriver.title 
  
# Printing the title of this URL 
print(get_title)








    
    


