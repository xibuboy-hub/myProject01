import requests
import time
day_dict={"d1":"f62","d5":"f164","d10":"f174"}
def get_bkzj1(day):
    cookies = {
        'qgqp_b_id': '29d140db32894ccaa56959d33a92435a',
        'st_si': '55353677014983',
        'st_asi': 'delete',
        'fullscreengg': '1',
        'fullscreengg2': '1',
        'st_pvi': '87339860201560',
        'st_sp': '2026-07-03%2016%3A03%3A12',
        'st_inirUrl': 'https%3A%2F%2Fwww.baidu.com%2Flink',
        'st_sn': '8',
        'st_psi': '20260706103750851-113300300820-2001608012',
    }

    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-CN;q=0.6',
        'Connection': 'keep-alive',
        'Referer': 'https://data.eastmoney.com/bkzj/hy.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Google Chrome";v="149", "Chromium";v="149", "Not)A;Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        # 'Cookie': 'qgqp_b_id=29d140db32894ccaa56959d33a92435a; st_si=55353677014983; st_asi=delete; fullscreengg=1; fullscreengg2=1; st_pvi=87339860201560; st_sp=2026-07-03%2016%3A03%3A12; st_inirUrl=https%3A%2F%2Fwww.baidu.com%2Flink; st_sn=8; st_psi=20260706103750851-113300300820-2001608012',
    }

    params = {
        'key': day_dict[day],
        'code': 'm:90+s:4',
    }

    response = requests.get('https://data.eastmoney.com/dataapi/bkzj/getbkzj', params=params, cookies=cookies, headers=headers)
    # for item in response.json()['data']['diff']:
    #      if item['f14']=='半导体':
    #          print(f"{time.strftime('%Y-%m-%d %H:%M:%S')}: {item['f14']}, {item['f62']}")
    #      continue
    data_list = response.json()['data']['diff']
    return data_list

if __name__ == "__main__":
    while True:
        print(get_bkzj1("d1"))
        time.sleep(20)  # 每隔20秒获取一次数据
