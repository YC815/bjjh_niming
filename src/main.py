from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import os
from dotenv import load_dotenv
load_dotenv()

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.instagram.com")


wait = WebDriverWait(driver, 10)

element_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"
element = wait.until(lambda driver: driver.find_element(By.XPATH, element_xpath))
element.send_keys("bjjh.niming.5")

element_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[2]/div/label/input"
element = wait.until(lambda driver: driver.find_element(By.XPATH, element_xpath))
element.send_keys(os.getenv("PASSWORD"))

element_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]"
element = wait.until(lambda driver: driver.find_element(By.XPATH, element_xpath))
element.click()


wait = WebDriverWait(driver, 10)

element_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[7]/div/span/div/a/div"
element = wait.until(lambda driver: driver.find_element(By.XPATH, element_xpath))
element.click()

driver.quit()
