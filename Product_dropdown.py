from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver= webdriver.Firefox()
driver.get("https://www.saucedemo.com")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@class='submit-button btn_action']").click()

Select(driver.find_element(By.XPATH,"//select[@class='product_sort_container']")).select_by_value("hilo")