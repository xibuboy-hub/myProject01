
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/3/6 17:36
*  @Project :   flask_01
*  @FileName:   app.py
**************************************
程式用途:
"""

from apps import create_app
from apscheduler.schedulers.blocking import BlockingScheduler
from demo_test.wether import job
app = create_app()


if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(job, 'cron', hour=8, minute=0)
    scheduler.start()
    app.run(host='0.0.0.0', port=5174)
