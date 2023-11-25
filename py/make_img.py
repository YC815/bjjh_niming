from PIL import Image, ImageDraw, ImageFont
from openai import OpenAI

client = OpenAI(api_key='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')



# 用戶和AI的訊息
user = "笑死今天好累"
ai_response = client.chat.completions.create(model="gpt-3.5-turbo",
messages=[
    {"role": "user", "content": "請在68字內簡單幽默的回答\"%s\"。" % (user)}
])
user = user.replace('\n', ' ')  # 將換行符替換為空格
user = [user[i:i + 14] for i in range(0, len(user), 14)]
user = "\n".join(user)

ai = ai_response.choices[0].message["content"].replace('\n', ' ')  # 將換行符替換為空格
ai = [ai[i:i + 17] for i in range(0, len(ai), 17)]
ai = "\n".join(ai)

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
