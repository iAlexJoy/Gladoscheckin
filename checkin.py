import requests
import json
import os

# -------------------------------------------------------------------------------------------
# github workflows
# -------------------------------------------------------------------------------------------
if __name__ == '__main__':

    cookies = os.environ.get("COOKIES", []).split("&")
    check_in_url = "https://glados.cloud/api/user/checkin"        # 签到地址
    status_url = "https://glados.cloud/api/user/status"          # 查看账户状态

    referer = 'https://glados.cloud/console/checkin'
    origin = "https://glados.cloud"
    useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    payload = {
        'token': 'glados.cloud'
    }
        
    for cookie in cookies:
        checkin = requests.post(check_in_url, headers={'cookie': cookie, 'referer': referer, 'origin': origin,
                                'user-agent': useragent, 'content-type': 'application/json;charset=UTF-8'}, data=json.dumps(payload))
        state = requests.get(status_url, headers={
                            'cookie': cookie, 'referer': referer, 'origin': origin, 'user-agent': useragent})
