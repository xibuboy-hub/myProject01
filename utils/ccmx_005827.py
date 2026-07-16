# 测试git
import requests
import json

def get_005827_fund_list():
    cookies = {
        'qgqp_b_id': '29d140db32894ccaa56959d33a92435a',
        'st_si': '65829302131755',
        'websitepoptg_api_time': '1783490184476',
        'EMFUND1': 'null',
        'EMFUND2': 'null',
        'EMFUND3': 'null',
        'EMFUND4': 'null',
        'EMFUND5': 'null',
        'EMFUND6': 'null',
        'st_nvi': 'BkB8ykT4TDuPH1v9rfiMP6028',
        'nid18': '0b594220aeabdae3a7b93459332249b9',
        'nid18_create_time': '1783494661037',
        'gviem': 'W9Cy6JrCLeqq87aVaVydcf1c7',
        'gviem_create_time': '1783494661037',
        'st_asi': 'delete',
        'EMFUND0': 'null',
        'EMFUND8': '07-09%2014%3A47%3A59@%23%24%u79D1%u521B%u82AF%u7247ETF%u6613%u65B9%u8FBE@%23%24589130',
        'fullscreengg': '1',
        'fullscreengg2': '1',
        'wsc_checkuser_ok': '1',
        'EMFUND9': '07-10%2010%3A24%3A41@%23%24%u6613%u65B9%u8FBE%u84DD%u7B79%u7CBE%u9009%u6DF7%u5408@%23%24005827',
        'EMFUND7': '07-10 10:37:18@#$%u6613%u65B9%u8FBE%u79D1%u521B%u82AF%u7247ETF%u8054%u63A5C@%23%24020671',
        'st_pvi': '22588096608539',
        'st_sp': '2026-07-08%2013%3A56%3A24',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '42',
        'st_psi': '20260710103824567-112200305283-8822655230',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://fundf10.eastmoney.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'qgqp_b_id=29d140db32894ccaa56959d33a92435a; st_si=65829302131755; websitepoptg_api_time=1783490184476; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; st_nvi=BkB8ykT4TDuPH1v9rfiMP6028; nid18=0b594220aeabdae3a7b93459332249b9; nid18_create_time=1783494661037; gviem=W9Cy6JrCLeqq87aVaVydcf1c7; gviem_create_time=1783494661037; st_asi=delete; EMFUND0=null; EMFUND8=07-09%2014%3A47%3A59@%23%24%u79D1%u521B%u82AF%u7247ETF%u6613%u65B9%u8FBE@%23%24589130; fullscreengg=1; fullscreengg2=1; wsc_checkuser_ok=1; EMFUND9=07-10%2010%3A24%3A41@%23%24%u6613%u65B9%u8FBE%u84DD%u7B79%u7CBE%u9009%u6DF7%u5408@%23%24005827; EMFUND7=07-10 10:37:18@#$%u6613%u65B9%u8FBE%u79D1%u521B%u82AF%u7247ETF%u8054%u63A5C@%23%24020671; st_pvi=22588096608539; st_sp=2026-07-08%2013%3A56%3A24; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=42; st_psi=20260710103824567-112200305283-8822655230',
    }

    response = requests.get(
        'https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&invt=2&fields=f2,f3,f12,f14,f9&cb=jQuery1830705786075454038_1783651104789&ut=267f9ad526dbe6b0262ab19316f5a25b&secids=1.600519,0.000858,0.000568,116.00700,116.09987,116.00883,1.600809,116.09988,116.06618,0.002027,0.300832,1.688617,&_=1783651190677',
        cookies=cookies,
        headers=headers,
    )
    json_data=json.loads(response.text.split('(')[1].split(')')[0])
    return json_data['data']['diff']

def get_020671_fund_list():
    cookies = {
        'qgqp_b_id': '29d140db32894ccaa56959d33a92435a',
        'st_si': '65829302131755',
        'websitepoptg_api_time': '1783490184476',
        'EMFUND1': 'null',
        'EMFUND2': 'null',
        'EMFUND3': 'null',
        'EMFUND4': 'null',
        'EMFUND5': 'null',
        'EMFUND6': 'null',
        'st_nvi': 'BkB8ykT4TDuPH1v9rfiMP6028',
        'nid18': '0b594220aeabdae3a7b93459332249b9',
        'nid18_create_time': '1783494661037',
        'gviem': 'W9Cy6JrCLeqq87aVaVydcf1c7',
        'gviem_create_time': '1783494661037',
        'st_asi': 'delete',
        'EMFUND0': 'null',
        'EMFUND8': '07-09%2014%3A47%3A59@%23%24%u79D1%u521B%u82AF%u7247ETF%u6613%u65B9%u8FBE@%23%24589130',
        'fullscreengg': '1',
        'fullscreengg2': '1',
        'wsc_checkuser_ok': '1',
        'EMFUND9': '07-10%2010%3A24%3A41@%23%24%u6613%u65B9%u8FBE%u84DD%u7B79%u7CBE%u9009%u6DF7%u5408@%23%24005827',
        'EMFUND7': '07-10 10:37:18@#$%u6613%u65B9%u8FBE%u79D1%u521B%u82AF%u7247ETF%u8054%u63A5C@%23%24020671',
        'st_pvi': '22588096608539',
        'st_sp': '2026-07-08%2013%3A56%3A24',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '43',
        'st_psi': '20260710104951296-112200305283-3063504577',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://fundf10.eastmoney.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'same-site',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'qgqp_b_id=29d140db32894ccaa56959d33a92435a; st_si=65829302131755; websitepoptg_api_time=1783490184476; EMFUND1=null; EMFUND2=null; EMFUND3=null; EMFUND4=null; EMFUND5=null; EMFUND6=null; st_nvi=BkB8ykT4TDuPH1v9rfiMP6028; nid18=0b594220aeabdae3a7b93459332249b9; nid18_create_time=1783494661037; gviem=W9Cy6JrCLeqq87aVaVydcf1c7; gviem_create_time=1783494661037; st_asi=delete; EMFUND0=null; EMFUND8=07-09%2014%3A47%3A59@%23%24%u79D1%u521B%u82AF%u7247ETF%u6613%u65B9%u8FBE@%23%24589130; fullscreengg=1; fullscreengg2=1; wsc_checkuser_ok=1; EMFUND9=07-10%2010%3A24%3A41@%23%24%u6613%u65B9%u8FBE%u84DD%u7B79%u7CBE%u9009%u6DF7%u5408@%23%24005827; EMFUND7=07-10 10:37:18@#$%u6613%u65B9%u8FBE%u79D1%u521B%u82AF%u7247ETF%u8054%u63A5C@%23%24020671; st_pvi=22588096608539; st_sp=2026-07-08%2013%3A56%3A24; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=43; st_psi=20260710104951296-112200305283-3063504577',
    }

    response = requests.get(
        'https://push2.eastmoney.com/api/qt/ulist.np/get?fltt=2&invt=2&fields=f2,f3,f12,f14,f9&cb=jQuery18304779624809181_1783651791363&ut=267f9ad526dbe6b0262ab19316f5a25b&secids=1.688521,1.688256,1.688072,1.688981,1.688041,1.688008,1.688012,1.688795,1.688234,1.688220,&_=1783651831433',
        cookies=cookies,
        headers=headers,
    )
    json_data=json.loads(response.text.split('(')[1].split(')')[0])
    return json_data['data']['diff']

if __name__ == '__main__':
    print(get_020671_fund_list())
    print(get_005827_fund_list())