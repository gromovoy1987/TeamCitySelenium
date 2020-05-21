from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/gromovoy/PycharmProjects/TeamCitySelenium/chromedriver")
aboutTab = "//*[text()='About']"
searchString = "I am searching Google"
driver.get("https://google.com")
driver.find_element(By.XPATH,aboutTab).click()
print(driver.title)
driver.quit()
