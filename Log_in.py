from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://www.saucedemo.com")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@class='submit-button btn_action']").click()

try:
    print(driver.find_element(By.CSS_SELECTOR,"div [class='app_logo']").text)
    print("Login Test Case is Passed")
    assert True
except NoSuchElementException:
    print("Login Test Case is Failed")
    assert False
driver.close()
