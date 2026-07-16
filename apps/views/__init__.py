# -*- coding: utf-8 -*-
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/3/7 10:40
*  @Project :   flask_01
*  @FileName:   __init__.py.py
**************************************
程式用途:
"""
from flask import Blueprint, redirect, url_for, render_template
import re, os
import pandas as pd

bp = Blueprint('index', __name__)


def find_second_number(text):
    # 使用正则表达式查找所有数字，并返回第二组
    numbers = re.findall(r'\d{8}', text)
    if len(numbers) >= 2:
        return numbers[1]  # 返回第二组数字
    else:
        return None  # 如果没有足够的数字组，返回None


@bp.route('/')
def index():
    return redirect(url_for('other.upph1'))


@bp.route('/video')
def move_new_operator_video():
    """
    移动新人视频中已离职人员视频
    :return:
    """
    work_dir = 'Y:/L3_公共資源/TNB SUB執法記錄視頻/New OP Training'
    em_df = pd.read_excel('Y:/Joy_Lo/backup_joy/每日人力定位/L3每日人力明細1.xlsx',
                          sheet_name='竖行架构', index_col=None)
    all_employ_no = em_df['工號'].tolist()
    child_employ_no = []
    with open(f'{work_dir}/list.txt') as p:
        lines = p.readlines()
        for line in lines:
            employ_no = find_second_number(line.replace('\n', ''))
            child_employ_no.append(employ_no)
    parent_set = set(all_employ_no)
    child_set = set(child_employ_no)
    off_employ_no = list(child_set - parent_set)
    for i in off_employ_no:
        for filename in os.listdir(work_dir):
            file_path = os.path.join(work_dir, filename)
            if i in filename:
                os.system(f'move /y "{file_path}" "Y:\\L3_公共資源\\TNB SUB執法記錄視頻\\離職人員"')
                print(f'{filename} move OK~')
            continue
    # 获取剩余文件个数
    n = len([filename for filename in os.listdir(work_dir) if filename.endswith('.mov'.upper())])
    print(f'视频文件清洗完毕，共移动{len(off_employ_no)}个人员视频。剩余视频{n}个')
    return f'视频文件清洗完毕，共移动{len(off_employ_no)}个人员视频。剩余视频{n}个'


if __name__ == '__main__':
    move_new_operator_video()
