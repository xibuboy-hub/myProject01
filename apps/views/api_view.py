# -*- coding: utf-8 -*-
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/3/7 19:03
*  @Project :   flask_01
*  @FileName:   api_view.py
**************************************
程式用途:
"""
import json, re
import requests
from flask import Blueprint, request, jsonify

#from utils.db_init import Access, Sqlite, Mysql

bp = Blueprint('api', __name__, url_prefix='/api')
#operate = Access()
#msq = Mysql('10.129.116.144', 'l3_fixture_management')
#data_new_db = Sqlite('./data/data_new.db')


@bp.route('/fanyi', methods=['GET'])
def fanyi():
    # 获取GET请求参数
    get_params = request.args.get('kw', 'hello')
    # 获取POST请求的JSON数据
    # post_data = request.get_json()['params']['kw'] if request.is_json else None
    # get=input("输入单词:")
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    }
    data = {
        'kw': get_params
    }
    proixse = {
        'https': '36.6.144.150:8089'
    }
    response = requests.post(url, headers=headers, data=data).json()

    # result = response['data'][0]['v']
    res_result = response['data']
    # print(result)
    return {'content': res_result}



# 检测待翻译语言
@bp.route('/detectedLanguage', methods=['post'])
def detectedLanguage():
    cookies = {
        'MUID': '1E8BEE76CE7669B12048FBC5CF2C6821',
        'SRCHD': 'AF=NOFORM',
        'SRCHUID': 'V=2&GUID=4EA292A78584401996632524E501C2F9&dmnchg=1',
        'BFBUSR': 'BFBHP=0',
        'MUIDB': '1E8BEE76CE7669B12048FBC5CF2C6821',
        'MMCASM': 'ID=06CC9B28C0584F0292F81907712650F5',
        '_clck': '1atuges%7C2%7Cfyb%7C0%7C2036',
        'USRLOC': 'HS=1&ELOC=LAT=31.344369888305664|LON=120.97618103027344|N=%E6%B1%9F%E8%98%87%E7%9C%81%20%E6%98%86%E5%B1%B1%E5%B8%82|ELT=4|',
        '_RwBf': 'r=0&ilt=30&ihpd=0&ispd=5&rc=39&rb=0&gb=&rg=200&pc=36&mtu=0&rbb=0&cid=0&clo=0&v=6&l=2025-11-28T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0&rwflt=0&rwaul2=0&g=&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2025-11-28T11:35:57.4265840+00:00&rwred=0&wls=&wlb=&wle=&ccp=&cpt=&lka=0&lkt=0&aad=0&TH=',
        '_UR': 'QS=0&TQS=0&Pn=1',
        '_HPVN': 'CS=eyJQbiI6eyJDbiI6MTAsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjEwLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNi0wMS0wOVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxOSwiVG9ibiI6MH0=',
        '_SS': 'SID=0E54DA532F166AF22E64CCAA2E4D6B1E',
        '_tarLang': 'default=vi',
        '_TTSS_OUT': 'hist=WyJlbiIsInpoLUhhbnMiLCJ2aSJd',
        'btstkn': 'd27HeTexJcK7QWBR6gYZz%252BOKXautbF%252BSfAnwT8gJ6I45I6PfL14vQnOZtRja3HmjcusIF7D3xScRQA3hTzV8QbZDxoM9eAeSMPQVXlMJ5Gk%253D',
        '_TTSS_IN': 'hist=WyJ6aC1IYW50IiwiemgtSGFucyIsImVuIiwiYXV0by1kZXRlY3QiXQ==&isADRU=1',
        '_EDGE_S': 'SID=0E54DA532F166AF22E64CCAA2E4D6B1E&mkt=zh-CN',
        'SRCHHPGUSR': 'SRCHLANG=zh-Hant&PV=15.0.0&HV=1770450872&HVE=CfDJ8HAK7eZCYw5BifHFeUHnkJH6UNmX6Fs2cNrlBZeSrbnNW94zKKGa5opyhlR-e5-SNRaX-9UzdlgZF17xAonnFdG3uqYbzCYh3kiMZGzwLecTuygcpqghjmdlrxqdgAyzeNgFS35dXcsek9gmn65xmnOkQJJIIIgoKTQfCLkBtLwKtzMz9eGuzae7Ma3rQvx9Pg&WTS=63886596843&DM=0&BRW=XW&BRH=S&CW=1536&CH=695&SCW=1536&SCH=695&DPR=1.3&UTC=480&PRVCW=1536&PRVCH=695&B=0&BZA=0&PREFCOL=0&EXLTT=24&WEBP=1&P=CfDJ8BJecyNyfxpMtsfDoM3OqQuYFwmMTzhBlhJF-8U1Qzyp5dD1iOath80-hlqlfq9AdLwjdMG_h8z0CXZ0bIgKL0wZRqGO47r7e3jg-0ipwFmdFyF7610TQ-jWHCeuTVRRv0AThzgLM00-4QRb2k2OIbgqRiownpatJwHZ9V5DWrzzKHPBnlPWJGlRVhtAmlFtxQ0',
        'SRCHUSR': 'DOB=20250320&T=1743504686000&DS=1',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'ect': '4g',
        'origin': 'https://www.bing.com',
        'priority': 'u=1, i',
        'referer': 'https://www.bing.com/translator?ref=TThis&&text=&from=&to=zh-CN&mkt=zh-CN',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"144.0.7559.133"',
        'sec-ch-ua-full-version-list': '"Not(A:Brand";v="8.0.0.0", "Chromium";v="144.0.7559.133", "Google Chrome";v="144.0.7559.133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        # 'cookie': 'MUID=1E8BEE76CE7669B12048FBC5CF2C6821; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=4EA292A78584401996632524E501C2F9&dmnchg=1; BFBUSR=BFBHP=0; MUIDB=1E8BEE76CE7669B12048FBC5CF2C6821; MMCASM=ID=06CC9B28C0584F0292F81907712650F5; _clck=1atuges%7C2%7Cfyb%7C0%7C2036; USRLOC=HS=1&ELOC=LAT=31.344369888305664|LON=120.97618103027344|N=%E6%B1%9F%E8%98%87%E7%9C%81%20%E6%98%86%E5%B1%B1%E5%B8%82|ELT=4|; _RwBf=r=0&ilt=30&ihpd=0&ispd=5&rc=39&rb=0&gb=&rg=200&pc=36&mtu=0&rbb=0&cid=0&clo=0&v=6&l=2025-11-28T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0&rwflt=0&rwaul2=0&g=&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2025-11-28T11:35:57.4265840+00:00&rwred=0&wls=&wlb=&wle=&ccp=&cpt=&lka=0&lkt=0&aad=0&TH=; _UR=QS=0&TQS=0&Pn=1; _HPVN=CS=eyJQbiI6eyJDbiI6MTAsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjEwLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNi0wMS0wOVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxOSwiVG9ibiI6MH0=; _SS=SID=0E54DA532F166AF22E64CCAA2E4D6B1E; _tarLang=default=vi; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiLCJ2aSJd; btstkn=d27HeTexJcK7QWBR6gYZz%252BOKXautbF%252BSfAnwT8gJ6I45I6PfL14vQnOZtRja3HmjcusIF7D3xScRQA3hTzV8QbZDxoM9eAeSMPQVXlMJ5Gk%253D; _TTSS_IN=hist=WyJ6aC1IYW50IiwiemgtSGFucyIsImVuIiwiYXV0by1kZXRlY3QiXQ==&isADRU=1; _EDGE_S=SID=0E54DA532F166AF22E64CCAA2E4D6B1E&mkt=zh-CN; SRCHHPGUSR=SRCHLANG=zh-Hant&PV=15.0.0&HV=1770450872&HVE=CfDJ8HAK7eZCYw5BifHFeUHnkJH6UNmX6Fs2cNrlBZeSrbnNW94zKKGa5opyhlR-e5-SNRaX-9UzdlgZF17xAonnFdG3uqYbzCYh3kiMZGzwLecTuygcpqghjmdlrxqdgAyzeNgFS35dXcsek9gmn65xmnOkQJJIIIgoKTQfCLkBtLwKtzMz9eGuzae7Ma3rQvx9Pg&WTS=63886596843&DM=0&BRW=XW&BRH=S&CW=1536&CH=695&SCW=1536&SCH=695&DPR=1.3&UTC=480&PRVCW=1536&PRVCH=695&B=0&BZA=0&PREFCOL=0&EXLTT=24&WEBP=1&P=CfDJ8BJecyNyfxpMtsfDoM3OqQuYFwmMTzhBlhJF-8U1Qzyp5dD1iOath80-hlqlfq9AdLwjdMG_h8z0CXZ0bIgKL0wZRqGO47r7e3jg-0ipwFmdFyF7610TQ-jWHCeuTVRRv0AThzgLM00-4QRb2k2OIbgqRiownpatJwHZ9V5DWrzzKHPBnlPWJGlRVhtAmlFtxQ0; SRCHUSR=DOB=20250320&T=1743504686000&DS=1',
    }
    q = request.get_json(silent=True)
    s = get_token()
    data = {
        'fromLang': 'auto-detect',
        'to': 'vi',
        'text': q['q'],
        'tryFetchingGenderDebiasedTranslations': 'true',
        'token': s['token'],
        'key': s['key'],
    }

    response = requests.post(
        f"https://www.bing.com/ttranslatev3?isVertical=1&&IG={s['ig']}&IID=translator.5026",
        # cookies=cookies,
        headers=headers,
        data=data,
    )
    print(response.text)
    return json.loads(response.text)[0]['detectedLanguage']['language']


@bp.route('/vn', methods=['post'])
def main_translate():
    cookies = {
        'MUID': '1E8BEE76CE7669B12048FBC5CF2C6821',
        'SRCHD': 'AF=NOFORM',
        'SRCHUID': 'V=2&GUID=4EA292A78584401996632524E501C2F9&dmnchg=1',
        'BFBUSR': 'BFBHP=0',
        'MUIDB': '1E8BEE76CE7669B12048FBC5CF2C6821',
        'MMCASM': 'ID=06CC9B28C0584F0292F81907712650F5',
        '_clck': '1atuges%7C2%7Cfyb%7C0%7C2036',
        'USRLOC': 'HS=1&ELOC=LAT=31.344369888305664|LON=120.97618103027344|N=%E6%B1%9F%E8%98%87%E7%9C%81%20%E6%98%86%E5%B1%B1%E5%B8%82|ELT=4|',
        '_RwBf': 'r=0&ilt=30&ihpd=0&ispd=5&rc=39&rb=0&gb=&rg=200&pc=36&mtu=0&rbb=0&cid=0&clo=0&v=6&l=2025-11-28T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0&rwflt=0&rwaul2=0&g=&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2025-11-28T11:35:57.4265840+00:00&rwred=0&wls=&wlb=&wle=&ccp=&cpt=&lka=0&lkt=0&aad=0&TH=',
        '_UR': 'QS=0&TQS=0&Pn=1',
        '_HPVN': 'CS=eyJQbiI6eyJDbiI6MTAsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjEwLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNi0wMS0wOVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxOSwiVG9ibiI6MH0=',
        '_SS': 'SID=0E54DA532F166AF22E64CCAA2E4D6B1E',
        '_tarLang': 'default=vi',
        '_TTSS_OUT': 'hist=WyJlbiIsInpoLUhhbnMiLCJ2aSJd',
        'btstkn': 'd27HeTexJcK7QWBR6gYZz%252BOKXautbF%252BSfAnwT8gJ6I45I6PfL14vQnOZtRja3HmjcusIF7D3xScRQA3hTzV8QbZDxoM9eAeSMPQVXlMJ5Gk%253D',
        '_TTSS_IN': 'hist=WyJ6aC1IYW50IiwiemgtSGFucyIsImVuIiwiYXV0by1kZXRlY3QiXQ==&isADRU=1',
        '_EDGE_S': 'SID=0E54DA532F166AF22E64CCAA2E4D6B1E&mkt=zh-CN',
        'SRCHHPGUSR': 'SRCHLANG=zh-Hant&PV=15.0.0&HV=1770451833&HVE=CfDJ8HAK7eZCYw5BifHFeUHnkJF2cvQOQ8BfHwKrbLttFntlnZ2Nf-t7SLa69q7xc2oXDEZDZld_VsIgKJ0sP8RkuZjQZA0FOAWH_6V3VjcwuF66rW5ERwezFxbmK9mvxN7F2aS1cbNEXnZKcXhERF-Thz1Igerfy51F-DlEJ5zjHjCD5rbk_roymW5yeTfFzs1T5A&WTS=63886596843&DM=0&BRW=XW&BRH=S&CW=1536&CH=695&SCW=1536&SCH=695&DPR=1.3&UTC=480&PRVCW=1536&PRVCH=695&B=0&BZA=0&PREFCOL=0&EXLTT=24&WEBP=1&P=CfDJ8BJecyNyfxpMtsfDoM3OqQuYFwmMTzhBlhJF-8U1Qzyp5dD1iOath80-hlqlfq9AdLwjdMG_h8z0CXZ0bIgKL0wZRqGO47r7e3jg-0ipwFmdFyF7610TQ-jWHCeuTVRRv0AThzgLM00-4QRb2k2OIbgqRiownpatJwHZ9V5DWrzzKHPBnlPWJGlRVhtAmlFtxQ0',
        'SRCHUSR': 'DOB=20250320&T=1743504686000&DS=1&POEX=W',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/x-www-form-urlencoded',
        'ect': '4g',
        'origin': 'https://www.bing.com',
        'priority': 'u=1, i',
        'referer': 'https://www.bing.com/translator?ref=TThis&&text=&from=&to=zh-CN&mkt=zh-CN',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-arch': '"x86"',
        'sec-ch-ua-bitness': '"64"',
        'sec-ch-ua-full-version': '"144.0.7559.133"',
        'sec-ch-ua-full-version-list': '"Not(A:Brand";v="8.0.0.0", "Chromium";v="144.0.7559.133", "Google Chrome";v="144.0.7559.133"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-model': '""',
        'sec-ch-ua-platform': '"Windows"',
        'sec-ch-ua-platform-version': '"15.0.0"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        # 'cookie': 'MUID=1E8BEE76CE7669B12048FBC5CF2C6821; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=4EA292A78584401996632524E501C2F9&dmnchg=1; BFBUSR=BFBHP=0; MUIDB=1E8BEE76CE7669B12048FBC5CF2C6821; MMCASM=ID=06CC9B28C0584F0292F81907712650F5; _clck=1atuges%7C2%7Cfyb%7C0%7C2036; USRLOC=HS=1&ELOC=LAT=31.344369888305664|LON=120.97618103027344|N=%E6%B1%9F%E8%98%87%E7%9C%81%20%E6%98%86%E5%B1%B1%E5%B8%82|ELT=4|; _RwBf=r=0&ilt=30&ihpd=0&ispd=5&rc=39&rb=0&gb=&rg=200&pc=36&mtu=0&rbb=0&cid=0&clo=0&v=6&l=2025-11-28T08:00:00.0000000Z&lft=0001-01-01T00:00:00.0000000&aof=0&ard=0001-01-01T00:00:00.0000000&rwdbt=0&rwflt=0&rwaul2=0&g=&o=2&p=&c=&t=0&s=0001-01-01T00:00:00.0000000+00:00&ts=2025-11-28T11:35:57.4265840+00:00&rwred=0&wls=&wlb=&wle=&ccp=&cpt=&lka=0&lkt=0&aad=0&TH=; _UR=QS=0&TQS=0&Pn=1; _HPVN=CS=eyJQbiI6eyJDbiI6MTAsIlN0IjowLCJRcyI6MCwiUHJvZCI6IlAifSwiU2MiOnsiQ24iOjEwLCJTdCI6MCwiUXMiOjAsIlByb2QiOiJIIn0sIlF6Ijp7IkNuIjoxMCwiU3QiOjAsIlFzIjowLCJQcm9kIjoiVCJ9LCJBcCI6dHJ1ZSwiTXV0ZSI6dHJ1ZSwiTGFkIjoiMjAyNi0wMS0wOVQwMDowMDowMFoiLCJJb3RkIjowLCJHd2IiOjAsIlRucyI6MCwiRGZ0IjpudWxsLCJNdnMiOjAsIkZsdCI6MCwiSW1wIjoxOSwiVG9ibiI6MH0=; _SS=SID=0E54DA532F166AF22E64CCAA2E4D6B1E; _tarLang=default=vi; _TTSS_OUT=hist=WyJlbiIsInpoLUhhbnMiLCJ2aSJd; btstkn=d27HeTexJcK7QWBR6gYZz%252BOKXautbF%252BSfAnwT8gJ6I45I6PfL14vQnOZtRja3HmjcusIF7D3xScRQA3hTzV8QbZDxoM9eAeSMPQVXlMJ5Gk%253D; _TTSS_IN=hist=WyJ6aC1IYW50IiwiemgtSGFucyIsImVuIiwiYXV0by1kZXRlY3QiXQ==&isADRU=1; _EDGE_S=SID=0E54DA532F166AF22E64CCAA2E4D6B1E&mkt=zh-CN; SRCHHPGUSR=SRCHLANG=zh-Hant&PV=15.0.0&HV=1770451833&HVE=CfDJ8HAK7eZCYw5BifHFeUHnkJF2cvQOQ8BfHwKrbLttFntlnZ2Nf-t7SLa69q7xc2oXDEZDZld_VsIgKJ0sP8RkuZjQZA0FOAWH_6V3VjcwuF66rW5ERwezFxbmK9mvxN7F2aS1cbNEXnZKcXhERF-Thz1Igerfy51F-DlEJ5zjHjCD5rbk_roymW5yeTfFzs1T5A&WTS=63886596843&DM=0&BRW=XW&BRH=S&CW=1536&CH=695&SCW=1536&SCH=695&DPR=1.3&UTC=480&PRVCW=1536&PRVCH=695&B=0&BZA=0&PREFCOL=0&EXLTT=24&WEBP=1&P=CfDJ8BJecyNyfxpMtsfDoM3OqQuYFwmMTzhBlhJF-8U1Qzyp5dD1iOath80-hlqlfq9AdLwjdMG_h8z0CXZ0bIgKL0wZRqGO47r7e3jg-0ipwFmdFyF7610TQ-jWHCeuTVRRv0AThzgLM00-4QRb2k2OIbgqRiownpatJwHZ9V5DWrzzKHPBnlPWJGlRVhtAmlFtxQ0; SRCHUSR=DOB=20250320&T=1743504686000&DS=1&POEX=W',
    }
    q = request.get_json(silent=True)
    s = get_token()
    data = {
        'fromLang': 'auto-detect',
        'to': q['target'],
        'text': q['q'],
        'tryFetchingGenderDebiasedTranslations': 'true',
        'token': s['token'],
        'key': s['key'],
    }
    response = requests.post(
        f"https://www.bing.com/ttranslatev3?isVertical=1&&IG={s['ig']}&IID=translator.5026",
        cookies=cookies,
        headers=headers,
        data=data,
    )
    return json.loads(response.text)[0]['translations'][0]


def get_token():
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36'
    }
    response = requests.get(url='https://www.bing.com/translator?ref=TThis&&text=&from=&to=vi&mkt=zh-CN',
                            headers=headers).text

    token_list = re.findall('var params_AbusePreventionHelper = \[(.*?),3600000\];',
                            response)
    # print(token_list)
    key = token_list[0].split(',')[0]
    token = token_list[0].split(',')[1].replace('"', '')
    ig = re.findall(',IG:"(.*?)",', response)[0]
    data_dict = {
        "key": key,
        "token": token,
        "ig": ig
    }
    return data_dict



@bp.route('/checkStation', methods=['post','get'])
def checkStation():
    headers = {
        'Accept': 'text/html1,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': '10.128.128.120:9092',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    sn = request.values.get('sn')
    params_getstation = {
        'sn': sn,
        'CUSTOMER': 'A31',
        'SITE': 'CN53',
        'LINE': 'I3FA31SUBK',
        'GROUP': 'CSPT',
        'STATUS': 'PASS',
        'EC': '4H02',
        'udf2': 'STID',
        'udf3': 'PASS'
    }
    params_getbom = {
        'sn': sn,
        'CUSTOMER': 'A31',
        'SITE': 'CN53',
        'LINE': 'I3FA31SUBK',
        'GROUP': 'VIS',
        'udf2': 'QT',
        'udf3': 'GETBOM'
    }
    resp_getstation = requests.get(f'http://10.128.128.120:9092/FMDI/BASICVCI/BasicStationPass.ashx', headers=headers,
                                   params=params_getstation)
    resp_getbom = requests.get(f'http://10.128.128.120:9092/FMDI/BASICVCI/BasicGetInfo.ashx', headers=headers,
                               params=params_getbom)
    if resp_getstation.status_code == 200:
        return jsonify({'code': 1, 'data': {"station": resp_getstation.text, "bom": resp_getbom.text}})
    else:
        return jsonify({'code': 0, 'msg': '获取数据出错，请重试~'})

if __name__ == '__main__':
    # columns = ['id', 'c_no', 'c_name', 'tel', 'fax', 'gender']
    # values = ['id', 'c_no', 'c_name', 'tel', 'fax', 'gender']
    # set_clause = ', '.join([f"{col} = %s" for col in columns]) % (1, '2', '3', '4', '5', '6')
    # print(str([f"{vol}" for vol in values]).replace('[', '(').replace(']', ')'))
    # print(set_clause)
    main_translate()
