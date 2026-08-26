
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
    #scheduler = BlockingScheduler()
    #scheduler.add_job(job, 'cron', hour=8, minute=0)
    #scheduler.start()
    #serve(app,host='0.0.0.0',port=5174,threads=4)
    #app.run(host='0.0.0.0', port=5174)
    run_simple('0.0.0.0',4000,app,use_reloader=False, use_debugger=False, threaded=True)
