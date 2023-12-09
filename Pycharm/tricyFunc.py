import time

from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace 'path/to/your/chromedriver' with the actual path to your ChromeDriver executable
# chrome_driver_path = '/Users/ULLASMASTI/Downloads/chromedriver-win32.exe'

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to a website
driver.get("https://rahulshettyacademy.com/locatorspractice/")

# Perform some actions
driver.implicitly_wait(10)
driver.find_element(By.ID, 'inputUsername').send_keys("rahul")
driver.find_element(By.NAME, "inputPassword").send_keys("hello123")
driver.find_element(By.CLASS_NAME, "signInBtn").click()
print(driver.find_element(By.CSS_SELECTOR, "p.error").text)
# driver.save_screenshot('ss.png')
driver.get_screenshot_as_file('screenshots.pdf')
driver.find_element(By.LINK_TEXT, 'Forgot your password?').click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "input[placeholder='Email']").send_keys("john@rsa.com")
driver.find_element(By.XPATH, "//input[@type='text'][2]").clear()
driver.find_element(By.CSS_SELECTOR, "input[type='text']:nth-child(3)").send_keys("john@gmail.com")
driver.find_element(By.XPATH, "//form/input[3]").send_keys("9864353253")
driver.find_element(By.CSS_SELECTOR, ".reset-pwd-btn").click()
print(driver.find_element(By.CSS_SELECTOR, "form p").text)
# driver.save_screenshot('\Python\screenshots\ss1.png')
driver.get_screenshot_as_file('screenshots.pdf')
driver.find_element(By.XPATH, "//div[@class='forgot-pwd-btn-conainer']/button[1]").click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "#inputUsername").send_keys("rahul")
driver.find_element(By.CSS_SELECTOR, "input[type*='pass']").send_keys("rahulshettyacademy")
driver.find_element(By.ID, "chkboxOne").click()
driver.find_element(By.XPATH, "//button[contains(@class,'submit')]").click()

# # Wait for a while to see the result (you might want to use explicit waits in a real scenario in seconds)
# driver.implicitly_wait(5)

# Print the current URL
print('Current URL:', driver.current_url)

# Close the browser window
# driver.close()
driver.quit()
