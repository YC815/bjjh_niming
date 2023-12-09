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
from instagrapi import Client

load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'))

# 用戶和AI的訊息
user = "第五次測試"
ai_response = client.chat.completions.create(model="gpt-3.5-turbo", messages=[
    {"role": "user", "content": "請在68字內簡單幽默的回答\"%s\"。" % (user)}
])
ai_response = re.search(r"content='(.*?)', role", str(ai_response))
ai = str(ai_response.group(1))
user = user.replace('\n', ' ')  # 將換行符替換為空格
user = [user[i:i + 14] for i in range(0, len(user), 14)]
user = "\n".join(user)
print(ai_response)
ai = ai.replace('\n', ' ')  # 將換行符替換為空格
ai = [ai[i:i + 17] for i in range(0, len(ai), 17)]
ai = "\n".join(ai)

# 打開圖片
image = Image.open('public/ins.jpg')
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
image.load()
background = Image.new("RGB", image.size, (255, 255, 255))
background.paste(image, mask=image.split()[3])  # 3 is the alpha channel

background.save('public/ready.jpg', 'JPEG', quality=80)
cl = Client()
cl.login(os.getenv('USERNAME'), os.getenv('PASSWORD'))
media = cl.photo_upload(
    "public/ready.jpg",
    "濱江匿名網5.0",
    extra_data={
        "custom_accessibility_caption": "alt text example",
        "like_and_view_counts_disabled": 0,
        "disable_comments": 0,
    }
)

media.dict()
