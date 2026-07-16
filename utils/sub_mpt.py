#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2026/1/28 下午 03:22
# @Author  : Joy_Lo
# @File    : sub_mpt.py
import requests
from lxml import etree
from requests_ntlm import HttpNtlmAuth
import random


def sub_mpt(shift):
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
        '__EVENTVALIDATION': '/wEWLwKzr7XQBgLY9LT6DwKuiI+wBQLFgru0BwKSm/KVAwKal+6jCQKSzfnKDALN96/ICgLN99eGCALnrfqiAwLnrfqiAwLzteXtBgL0yPP9BwL3yOehDwLtlNmMDQLtlNmMDQLbiN3xDwL6iN3xDwLH4q6MDQKjy93MDwKcq/SQAQKGneznCAK/9t3MDwKgtLrIDwKisOXBDQKcsOXBDQKgvphvAqC+mG8CmazihwUCmazihwUC5Y+ikwwC04LWKQK7+6xEArv7rEQCiebu4AMCieaCjQoCiea2qgECieaq1wkCiebecwKJ5vKYBwKJ5ubFDwKJ5tqcAQKJ5s65CAKJ5uJmAonmloMHAsGVzZQBAov36vcPO6oBdz8UtI+RtTAaOWeSvAIN/mY=',
        # '__EVENTVALIDATION': valid_args,
        'ctl00$dr_Language': 'zh-tw',
        'ctl00$MainContent$drPlant': 'KSP3',
        'ctl00$MainContent$drCustNo': 'A31',
        'ctl00$MainContent$drProcess': 'SUB',
        'ctl00$MainContent$SelectClassNo1$drClassNo': shift,
        'ctl00$MainContent$drFloor': '',
        'ctl00$MainContent$drDeptGroup': 'IPQC',
        'ctl00$MainContent$drLineDesc': '',
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
    # print(resp.text)
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
    sub_mpt()
