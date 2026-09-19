
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/3/6 17:36
*  @Project :   flask_01
*  @FileName:   app.py
**************************************
程式用途:
"""

import os,sys
from apps import create_app
from apscheduler.schedulers.blocking import BlockingScheduler
from demo_test.wether import job
from waitress import serve
from werkzeug.serving import run_simple

# 获取当前文件所在的目录
current_dir = os.path.dirname(os.path.abspath(__file__))
# 添加当前目录到 sys.path 中
sys.path.append(current_dir)


app = create_app()

if __name__ == '__main__':
    # scheduler = BlockingScheduler()
    # scheduler.add_job(job, 'cron', hour=8, minute=0)
    # scheduler.start()

    # run_simple('0.0.0.0',4000,app,use_reloader=False, use_debugger=False, threaded=True)
    # 增加线程数以应对并发阻塞

    # channel_timeout: 通道超时时间，防止死连接占用线程
    # cleanup_interval: 清理间隔，释放资源
    serve(
        app,
        host='0.0.0.0',
        port=5174,
        threads=16,          # 根据 CPU 和内存适当增加，默认4可能不足
        channel_timeout=120,
        cleanup_interval=30,
        max_request_body_size=1073741824  # 1GB，避免大上传阻塞
    )
