import os
import re
import requests

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://ksmes2.compal.com',
    'pragma': 'no-cache',
    'priority': 'u=0, i',
    'referer': 'https://ksmes2.compal.com/Default?autologin=false',
    'sec-ch-ua': '"Google Chrome";v="135", "Not-A.Brand";v="8", "Chromium";v="135"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36',
    # 'cookie': 'LastLoginDB=A31; MESWeb.LoginMode=0; MESWeb.UserID=joy_lo; MESWeb.Password=; MESWeb.Domain=gi.compal.com',
}

params = {
    'autologin': 'false',
}

url = 'https://ksmes2.compal.com/Default'


def pp_url() -> list:
    _resp = requests.get(url, headers=headers)
    _resp.encoding = 'utf-8'
    obj = re.compile(
        r'id="__VIEWSTATE" value="(?P<_VIEWSTATE>.*?)" />.*?id="__EVENTVALIDATION" value="(?P<_EVENTVALIDATION>.*?)" />',
        re.S)
    _VIEWSTATE = obj.search(_resp.text).group("_VIEWSTATE")
    _EVENTVALIDATION = obj.search(_resp.text).group("_EVENTVALIDATION")
    data = {
        '__LASTFOCUS': '',
        'ToolkitScriptManager1_HiddenField': '',
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        # '__VIEWSTATE': '/rIPHZgZCqZsvgIVqYqH+SeyTxcQohDQfI40Jyj8ud6p96NGuwEyw84/pCIexpuIJ6484f+NEaUNRlZwcgklzvaxO6V7FCmmt4sUNCEeDC2Yyo+XJg6HYhqWhRBjkFFe/FsG0JjhqsY+F4uW3rKuxUaSwQ3Puj9c/KYbgsBwbpqKJL6Mg2rmBk3+l6D2U4ou3+s+fcfE/gOn3/NmwnGo84HEDR2PRdgQNSeBaOwWg7/zzXgn8HKdMDpZGjLEseMVHVHanJUfsIlGhEqlTOl3UVWqBxdlbqk7OQ8rviZscXARZx/ID6YffBv6GlY3dwy1',
        '__VIEWSTATE': _VIEWSTATE,
        '__VIEWSTATEGENERATOR': 'CA0B0334',
        # '__EVENTVALIDATION': 'q+qwcc2x3bikuGXvutUgElsE/wykFrHoR/iLpDr0nxlQwiUDH9STjE1PHe0DLXIsn8DHxlmZihwsQZCp8i3D17k/dhtqRsMZprBJ7j8ccHDutt9jktwlaF6vq3TaasZAftGzluCGA98H4ltNHlbgXF21EIuBVuQL5kCLjDGzWSPMLoDvlb3K8p8yE5TjWwZsKSN87lRqeRNJY+OAyidf5nJqtoCuVxk6qaAVb18oHIY5ZC+PdKzGHjAS0FKlbm80',
        '__EVENTVALIDATION': _EVENTVALIDATION,
        'txbNTUser': 'joy_lo',
        'txbNTPwd': 'compql123@',
        'ddlDomain': 'gi.compal.com',
        'btnLogin': 'Login',
    }
    #print(requests.post(url, params=params, headers=headers, data=data, allow_redirects=False).headers)
    resp = requests.post(url, params=params, headers=headers, data=data, allow_redirects=False).headers['location']

    resp_second = \
        requests.get(resp, headers=headers, allow_redirects=False).headers['location']
    part_url = resp.split('login')[0][:-1] + resp_second
    resp_third = requests.get(part_url, headers=headers, allow_redirects=False).headers['location']

    # 登陆成功的url
    login_success = resp.split('login')[0][:-1] + resp_third
    # 登陆成功的response
    resp_success = requests.get(login_success, headers=headers).status_code

    # 加密字符串
    encrypt_str = resp_third.split('/')[1]

    url1 = resp.split('login')[0][:-1] + '/' + encrypt_str + '/QCM/bQCM0301A31.aspx'
    hed = {
        'referer': login_success,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36'
    }
    resp_qcm = requests.get(url1, headers=hed).status_code
    # print(resp_qcm)
    return [url1, resp_success, ]


if __name__ == '__main__':
    print(pp_url())
