from flask import Flask, render_template_string
from db import get_all_messages

app = Flask(__name__)

TEMPLATE = '''
<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
    <meta charset="utf-8">
    <meta http-equiv="Content-Language" content="fa">
    <title>پنل مدیریت چت‌بات</title>
    <style>
        body { font-family: Tahoma, sans-serif; direction: rtl; margin: 20px; background: #f5f5f5; }
        .msg { padding: 10px; margin-bottom: 10px; border-radius: 5px; background: #fff; box-shadow: 0 0 5px #ccc; }
        .user { color: blue; }
        .bot { color: green; }
    </style>
</head>
<body>
    <h2>📋 پیام‌ها</h2>
    {% for m in messages %}
        <div class="msg">
            <strong class="{{ m[2] }}">{{ m[2] }}</strong>: {{ m[3] }}
        </div>
    {% endfor %}
</body>
</html>
'''

@app.route("/")
def index():
    messages = get_all_messages()
    return render_template_string(TEMPLATE, messages=messages)

if __name__ == "__main__":
    app.run(debug=True)