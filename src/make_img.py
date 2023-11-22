from flask import Flask, request, jsonify

app = Flask(__name__)

# 定义一个用于处理POST请求的路由


@app.route('/processData', methods=['POST'])
def process_data():
    try:
        # 从请求中获取JSON数据
        data = request.get_json()
        text = data.get('text')

        print(text)
        return jsonify({"result": text})

    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == '__main__':
    app.run(debug=True)
