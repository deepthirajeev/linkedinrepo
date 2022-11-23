import parameters
from time import sleep
import json


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def linked_in_login():
   driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
   driver.get('https://www.linkedin.com/login')

   sleep(10)
   username = driver.find_element(By.ID, 'username')
   username.send_keys(parameters.linkedin_username)
   sleep(0.5)

   password = driver.find_element(By.ID, 'password')
   password.send_keys(parameters.linkedin_password)
   sleep(0.5)

   sign_in_button = driver.find_element(By.XPATH, '//*[@type="submit"]')
   sign_in_button.click()
   sleep(0.5)

   my_network= driver.find_element(By.XPATH, '//span[@title="My Network"]')
   my_network.click()

   sleep(10)

   my_connections = driver.find_element(By.XPATH, '//div[text()="Connections"]')
   my_connections.click()

   sleep(10)

   connectionnames= driver.find_elements(By.XPATH, '//div[@class="mn-connection-card__details"]//span[2]')
   connectionjob= driver.find_elements(By.XPATH, '//div[@ class="mn-connection-card__details"]//span[4]')
   result = {}
   index = 0  # Python's indexing starts at zero
   connections = []
   for item in connectionnames:  # Python's for loops are a "for each" loop
      print(connectionnames[index].text)
      print(connectionjob[index].text)
      connections.append({"connection_name": connectionnames[index].text, "connection_name": connectionjob[index].text})
      index += 1

   print(json.loads(json.dumps(connections)))
   driver.quit()
   return json.loads(json.dumps(connections))




