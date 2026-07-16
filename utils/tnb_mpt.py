#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/1/28 下午 03:21
# @Author  : Joy_Lo
# @File    : tnb_mpt.py

import requests
from lxml import etree
from requests_ntlm import HttpNtlmAuth
import random


def tnb_mpt(shift):
    cookies = {
        'ASP.NET_SessionId': 'rdve2y55wmrpp255gpfjcu45',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'zh-TW,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://ksphmsap.compal.com:5050',
        'Referer': 'https://ksphmsap.compal.com:5050/hms/Function_MPT/MPT170.aspx',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not;A=Brand";v="99", "Google Chrome";v="139", "Chromium";v="139"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'ASP.NET_SessionId=rdve2y55wmrpp255gpfjcu45',
    }

    data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        '__LASTFOCUS': '',
        '__VIEWSTATE': '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',
        # '__VIEWSTATE': args,
        '__VIEWSTATEGENERATOR': '34561B8F',
        '__EVENTVALIDATION': '/wEWHgLOo/KEDALY9LT6DwKuiI+wBQLFgru0BwKSm/KVAwKal+6jCQKSzfnKDALN96/ICgLN99eGCALnrfqiAwLnrfqiAwLzteXtBgL0yPP9BwL3yOehDwLtlNmMDQLtlNmMDQKjy93MDwKhtObIDwKisOXBDQKcsOXBDQKgvphvAuyep6sCApms4ocFApms4ocFAuWPopMMAtOC1ikC9sPE9wkCu/usRALBlc2UAQKL9+r3D2g4fAM2aRz8vh26XPDlt4SsoIUe',
        # '__EVENTVALIDATION': valid_args,
        'ctl00$dr_Language': 'zh-tw',
        'ctl00$MainContent$drPlant': 'KSP3',
        'ctl00$MainContent$drCustNo': 'KS3TNB',
        'ctl00$MainContent$drProcess': 'TNB',
        'ctl00$MainContent$SelectClassNo1$drClassNo': shift,
        'ctl00$MainContent$drFloor': 'TNB',
        'ctl00$MainContent$drDeptGroup': 'IPQC',
        'ctl00$MainContent$butSearch': '查詢',
    }
    accounts=[
        {"username":"Dick_Zhao","password":"Awsxedcrfv90!@"},{"username":"Timl_Li","password":"EDCRFV098~"}
        ]
    account=random.choice(accounts)
    resp = requests.post(
        'https://ksphmsap.compal.com:5050/hms/Function_MPT/MPT170.aspx',
        cookies=cookies,
        headers=headers,
        data=data,
        auth=HttpNtlmAuth(f'gi\\{account["username"]}', f'{account["password"]}')
    )
    et = etree.HTML(resp.text)
    data = et.xpath('//table[@id="ctl00_MainContent_GridView1"]/tr')
    n = 0
    for item in data[1:]:
        if item.xpath("./td")[4].text.strip() != '' and item.xpath("./td")[8].text.strip() == '':
            n = n + 1
            # print(f'{n}.{item.xpath("./td/text()")}')
    resp.close()
    print([i.xpath("./td/text()") for i in data[1:]])
    return {'code': 0, 'data': [i.xpath("./td/text()") for i in data[1:]], 'qty': n,"username":account["username"]}


if __name__ == '__main__':
    tnb_mpt()
