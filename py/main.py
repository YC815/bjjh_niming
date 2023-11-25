from selenium.webdriver.common.action_chains import ActionChains
from dotenv import load_dotenv
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium import webdriver
from flask import Flask, request, jsonify
from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI
import re
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

load_dotenv()
client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))


def wait_for_clickable(driver, locator, timeout):
    try:
        WebDriverWait(driver, timeout, 1).until(
            EC.element_to_be_clickable(locator))
        # return True
    except TimeoutException:
        print("Wait TimeoutException:%s" % str(locator))
        # return False


# 打開圖片
image = Image.open('public/ins.png')
draw = ImageDraw.Draw(image)

# 加載一個支持中文的字體
font_path = "public/NotoSansTC-Regular.ttf"  # 替換成你的中文字體路徑
font = ImageFont.truetype(font_path, size=66)  # 設置字體大小

# 繪制文本
text_position_user = (50, 66)  # 調整文字的位置
text_color = 'rgb(255, 255, 255)'  # 設定文字顏色
draw.text(text_position_user, user, fill=text_color, font=font)

font = ImageFont.truetype(font_path, size=56)
text_position_ai = (50, 700)  # 調整文字的位置
draw.text(text_position_ai, ai, fill=text_color, font=font)

# 保存圖片
image.save('public/ready.png')

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://www.instagram.com")


wait = WebDriverWait(driver, 10)

element_xpath = "/html/body/div[2]/div/div/div[2]/div/div/div/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[1]/div/label/input"
element = wait.until(lambda driver: driver.find_element(By.XPATH, element_xpath))
element.send_keys(os.getenv("USERNAME"))

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

wait = WebDriverWait(driver, 10)
element_xpath = "/html/body/div[10]/div[1]/div/div[3]/div/div/div/div/div/div/div/div[2]/div[1]/div/div/div[2]/div/button"

wait_for_clickable(driver, (By.XPATH, element_xpath), 10)
imgInput = driver.find_element(By.XPATH, element_xpath)
imgInput.send_keys('public/ready.png')

driver.quit()
