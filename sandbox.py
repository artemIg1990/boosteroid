from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://stage.boosteroid.com/")
time.sleep(10)

driver.save_screenshot(f"Login_page_{time.strftime("%%H_%M_%S")}.png")
print(f"Login_page {time.strftime("%y_%m_%d_%H:%M:%S")}")