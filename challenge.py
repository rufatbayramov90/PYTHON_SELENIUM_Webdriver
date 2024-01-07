from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")
# Find the first name, last name, and email fields
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")

# Fill out the form
first_name.send_keys("Rufo")
last_name.send_keys("Bayram")
email.send_keys("rufatbyrmv@gmail.com")

#locate the Sign Up button then click on it
submit = driver.find_element(By.CSS_SELECTOR, value="from button")
submit.click()


