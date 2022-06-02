import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://www.google.com/")
assert "Google" in driver.title
searchbar = driver.find_element(by="name", value="q")
searchbar.clear()
searchbar.send_keys("Pacman")
searchbar.send_keys(Keys.RETURN)
driver.find_element(by=By.XPATH, value='(//h3)[1]/../../a').click()

moves = [Keys.LEFT, Keys.RIGHT, Keys.UP,Keys.DOWN]
while True:
    driver.find_element(by=By.CSS_SELECTOR, value="iframe").send_keys(random.choice(moves))

