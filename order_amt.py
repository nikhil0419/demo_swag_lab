from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

driver= webdriver.Firefox()
driver.get("https://www.saucedemo.com")
driver.find_element(By.ID,"user-name").send_keys("standard_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.XPATH,"//input[@class='submit-button btn_action']").click()

# Add_Item --> Sauce Labs Backpack
driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Backpack']").click()
# Add_To_Cart
driver.find_element(By.XPATH,"//button[@id='add-to-cart']").click()
#Back_To_Products
driver.find_element(By.XPATH,"//button[@id='back-to-products']").click()

# Add_Item --> Sauce Labs Bike Light
driver.find_element(By.XPATH,"//div[normalize-space()='Sauce Labs Bike Light']").click()
# Add_To_Cart
driver.find_element(By.XPATH,"//button[@id='add-to-cart']").click()
#Back_To_Products
driver.find_element(By.XPATH,"//button[@id='back-to-products']").click()

# Click_Shopping_Cart_Link
driver.find_element(By.XPATH,"//a[@class='shopping_cart_link']").click()

# Checkout
driver.find_element(By.XPATH,"//button[@id='checkout']").click()

# Enter_First_Name
driver.find_element(By.XPATH,"//input[@id='first-name']").send_keys("Nikhil")
# Enter_Last_Name
driver.find_element(By.XPATH,"//input[@id='last-name']").send_keys("kar")
# Enter_Zip/Postal Code
driver.find_element(By.XPATH,"//input[@id='postal-code']").send_keys("440012")
# Click_on_continue
driver.find_element(By.XPATH,"//input[@id='continue']").click()
# Click_on_finish
driver.find_element(By.XPATH,"//button[@id='finish']").click()

# Order_complete
try:
    print(driver.find_element(By.XPATH,"//h2[@class='complete-header']").text)
    driver.save_screenshot("Swag_Labs.png")
    driver.close()
    assert True
except:
    driver.close()
    assert False



