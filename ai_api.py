import requests

def ask_gpt(prompt):
    url = "https://api.aivix.app/api/gpt"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": prompt,
        "model": "gpt-3.5-turbo"
    }
    try:
        response = requests.post(url, json=data, headers=headers)
        return response.json().get("response", "متأسفم، پاسخی دریافت نشد.")
    except Exception as e:
        return "خطا در ارتباط با هوش مصنوعی."