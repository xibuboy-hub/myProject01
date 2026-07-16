import requests
import json
import time
import re
from apscheduler.schedulers.blocking import BlockingScheduler

# ================= 配置区域 =================
# 1. 企业微信群机器人 Webhook 地址 (请在企业微信群设置中获取)
WEBHOOK_URL = "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key=dd392623-4878-474c-8bec-9e93b192abfc"

# 2. 百度地图 API AK (请前往 http://lbsyun.baidu.com/ 申请)
BAIDU_AK = "YOUR_BAIDU_AK_HERE"

# 3. 目标城市 (中文，如: 北京, 上海)
CITY_NAME = "昆山"
# ===========================================


def get_baidu_weather(city):
    """
    调用百度地图API获取指定城市最近一周的天气信息
    """
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36"}
    # 百度地图天气API接口
    url = f"https://weathernew.pae.baidu.com/weathernew/pc?query={city}天气&srcid=4982"

    try:
        response = requests.get(url, headers=headers, timeout=10)
        data = response.text
        pattern = r'<script>(.*?)</script>'
        scripts = re.findall(pattern, data, re.DOTALL)[0].replace(".", "_", 1)
        wether_data = json.loads(scripts[17:-1])

        current_weather = wether_data["15_day_forecast"]['info']
        # print(current_weather)

        # 构建未来几天的天气列表 (百度API通常返回4-5天数据，包含当天)
        forecast_list = []
        for day_data in current_weather:
            forecast_list.append({
                "date": day_data['date'],
                "weather": day_data["weather_day"],
                "temperature": day_data['temperature_day'],
                "wind": day_data['wind_power_day']
            })
        return forecast_list, None

    except Exception as e:
        return None, str(e)


def format_message(forecast_list):
    """
    将天气数据格式化为Markdown消息
    """
    if not forecast_list:
        return "暂无天气数据"

    today = forecast_list[0]
    header = f"📅 **{today['date']} {CITY_NAME} 天气日报**\n"
    header += f"🌤 **今日**: {today['weather']} | 🌡 {today['temperature']}\n"
    header += f"💨 **风力**: {today['wind']}\n"
    header += "------------------------------\n*****未来几天预报:*****\n\n"

    body = ""
    # 跳过第一天（今天），展示后续几天
    for day in forecast_list[1:]:
        # 清理日期字符串中的星期几，保持简洁
        date_clean = day['date'].replace('(', '').replace(')', '')
        body += f"🔹 **{date_clean}**: {day['weather']} {day['temperature']}\n"
    # print(header+body)
    return header+body


def send_to_wechat(content):
    """
    发送Markdown消息到企业微信群
    """
    headers = {'Content-Type': 'application/json'}
    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }

    try:
        resp = requests.post(WEBHOOK_URL, headers=headers,
                             data=json.dumps(payload))
        result = resp.json()
        if result.get('errcode') == 0:
            print("消息发送成功")
        else:
            print(f"消息发送失败: {result}")
    except Exception as e:
        print(f"发送请求异常: {e}")


def job():
    """
    定时任务执行函数
    """
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] 开始执行天气推送任务...")
    forecast, error = get_baidu_weather(CITY_NAME)

    if error:
        send_to_wechat(f"⚠️ **天气推送异常**\n\n错误信息: {error}")
        print('error')
    else:
        msg_content = format_message(forecast)
        send_to_wechat(msg_content)
        print(msg_content)


if __name__ == '__main__':
    # 初始化调度器
    scheduler = BlockingScheduler()

    # 添加定时任务：每天早上 8:00 执行
    # cron 表达式: hour=8, minute=0
    scheduler.add_job(job, 'cron', hour=8, minute=0)

    print("调度器已启动，等待每天早上8点推送天气...")
    print("按 Ctrl+C 退出")

    try:
        scheduler.start()
    # forecast, error = get_baidu_weather(CITY_NAME)
    # format_message(forecast)
    except (KeyboardInterrupt, SystemExit):
        scheduler.shutdown()
