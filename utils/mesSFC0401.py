#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/8/23 下午 04:12
# @Author  : Joy_Lo
# @File    : mesSFC0401.py
import re

import requests
from utils.mesLogin import pp_url
import base64
import chardet


def get_args_view():
    url = pp_url()[0].rsplit('/', 2)[0] + '/SFC/bSFC0401A31.aspx'
    resp_text = requests.get(url).text
    obj = re.compile('<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(?P<vie>.*?)" />', re.S)
    args_view = re.search(obj, resp_text).group('vie')
    return args_view


def get_data(box_id):
    url = pp_url()[0].rsplit('/', 2)[0] + '/SFC/bSFC0401A31.aspx'

    headers = {
        'referer': url,
        'cookie': 'MESWeb.LoginMode=0; MESWeb.UserID=dick_zhao; MESWeb.Password=; MESWeb.Domain=gi.compal.com; LastLoginDB=A31',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36',
    }

    data = {
        '__EVENTTARGET': 'btQuery',
        '__EVENTARGUMENT': '',
        '__VIEWSTATE': f'{get_args_view()}',
        '__VIEWSTATEGENERATOR': '797ECB20',
        'tbCarton': f'{box_id}',
        'tbMONO': '',
        'AjaxCalendar1': '2025/07/23',
        'wtp1': '00:01',
        'wtp1Hour': '00',
        'wtp1Minute': '01',
        'tbPN': '',
        'AjaxCalendar2': '2025/08/23',
        'wtp2': '23:59',
        'wtp2Hour': '23',
        'wtp2Minute': '59',
        'tbPOLine': '',
        'tbSNList': '',
        'rblStatus': 'ALL',
        'tbNextStation': '',
        'rblSSM': 'SN',
        'tbGroup': '',
        'tbPO': '',
        'rblError': 'ALL',
        'tbLine': '',
        'rbCFI': 'ALL',
        'tbMFGSN': '',
        'wddlModel': '1',
        'tbContainer_no': '',
        'tbPallet_NO': '',
        'wddlPageselect': '0',
        'tbtrack_no': '',
    }

    response = requests.post(
        url,
        headers=headers,
        data=data,
    )
    obj_first_view = re.compile('<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="(?P<vie>.*?)" />', re.S)
    __view = re.search(obj_first_view, response.text).group('vie')
    ret = base64.b64decode(__view).decode(chardet.detect(base64.b64decode(__view))['encoding'])
    obj2 = re.compile(
        r'<SERIAL_NUMBER>(?P<sn>.*?)</SERIAL_NUMBER>.*?<INPUT_LINE>(?P<line>.*?)</INPUT_LINE>.*?<MODEL_NAME>(?P<model>.*?)</MODEL_NAME>.*?<CARTON_NO>(?P<box_id>.*?)</CARTON_NO>',
        re.S)
    ret2 = re.finditer(obj2, ret)
    result_list = []
    for i in ret2:
        print({"model": i['model'], "sn": i['sn'], "line": i['line'], "box_id": i['box_id']})
        result_list.append({"model": i['model'], "sn": i['sn'], "line": i['line'], "box_id": i['box_id']})
    return result_list


if __name__ == '__main__':
    get_data('3S129601296058P0900520J1Y4K11')
    # get_args_view()
