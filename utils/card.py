import requests
import time
from requests_ntlm import HttpNtlmAuth
import xml.etree.ElementTree as ET
def get_line_name():
    cookies = {
        "ASP.NET_SessionId":"e0cfnifnntjpgxjuymfh54yk"
    }
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0'
    }
    line_response = requests.get(
        'http://kspscap.gi.compal.com/efsline/LineSelection.aspx',
        cookies=cookies,
        headers=headers,
        verify=False,
        auth=HttpNtlmAuth('gi\\joy_lo', 'compql123!')
    )
    print(line_response.text)
    return line_response.text

def card_record(no,linename):
    cookies = {
        'ASP.NET_SessionId': 'hnw4g1551he42prw0tla5hvo',
        'lineid': 'lineid=6278',
    }
    timestamp = int(time.time() * 1000)
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'If-Modified-Since': '0',
        'Referer': 'http://kspscap.gi.compal.com/efsline/Answer.aspx',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0',
        #'Cookie': 'ASP.NET_SessionId=hnw4g1551he42prw0tla5hvo; lineid=lineid=6278',
    }
    lineID=linename.split('-')[0]
    line=linename.split('-')[1]
    params = {
        'empId': '',
        'UserNo': no,
        'ip': '10.129.236.219',
        'ntname': 'JOY_LO',
        'computer': 'NA',
        'Plant': 'KSP3',
        'Area': 'A31',
        'Line': line,
        'PlantId': '4',
        'AreaId': '3365',
        'LineId': lineID,
        'lockYN': 'N',
        'timestamp': timestamp,
    }

    response = requests.get(
        'http://kspscap.gi.compal.com/efsline/Handler.ashx',
        params=params,
        cookies=cookies,
        headers=headers,
        verify=False,
        auth=HttpNtlmAuth('gi\\chuang_nian', 'Bn155825!')
    )
    root = ET.fromstring(response.text)
    flag=bool(int(root.find('.//FLAG').text))
    # print(response.text)
    # if '<FLAG>0</FLAG>' in response.text:
    #     return False
    # return True
    if flag:
        username=root.find('.//UserName').text
        return True,username
    else:
        return False,None

if __name__=="__main__":
    # while True:
    #     card_no=input("输入工号开始刷卡:\n")
    #     if card_record(card_no):
    #         print("刷卡OK")
    #     else:
    #         print("工号错误！")
    get_line_name()
