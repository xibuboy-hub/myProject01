#! /usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/12/18 下午 04:19
# @Author  : Joy_Lo
# @File    : schedule.py
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler
from apps.views import other_view as ot


class DataCollector:
    def __init__(self, upph):
        self.upph = upph

    scheduler = BlockingScheduler()
    # 配置文件
    config_schedule = {
        "schedule": [
            {
                "hour": 7,
                "minute": 59
            },
            {
                "hour": 19,
                "minute": 59
            }
        ]
    }

    def run_collection(self):
        """执行采集任务"""
        print(f"Starting collection at {datetime.now()}")
        ot.add_upph(self.upph)

    def start(self):
        """启动定时任务"""
        for job in self.config_schedule['schedule']:
            self.scheduler.add_job(
                self.run_collection,
                trigger='cron',
                **job
            )
        self.scheduler.start()


if __name__ == '__main__':
    # collector = DataCollector()
    # collector.start()
    pass

