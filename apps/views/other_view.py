# -*- coding: utf-8 -*-
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/3/7 18:48
*  @Project :   flask_01
*  @FileName:   other_view.py
**************************************
程式用途:
"""
import datetime
import json
import xml.etree.ElementTree as ET
import re
import requests
from lxml import etree
from flask import Blueprint, request, render_template, send_from_directory, jsonify, Response
from requests_ntlm import HttpNtlmAuth
from utils.Pagination import Pagination
#from utils.db_init import Access, Sqlite
import utils.mesRepair211 as mes211
import utils.mes2161_n as mes_n
import utils.assy_mes216 as assy_mes
from utils.mesSFC0401 import get_data
# MPT查询
from utils.tnb_mpt import tnb_mpt
from utils.sub_mpt import sub_mpt
# 刷卡
from utils.card import card_record
from utils.encrypt import aes_decrypt
from utils.wrapper import login_reguired

from utils.mesLogin import pp_url

from utils.fail_qty_211 import parse_fail_part,get_fail_qty,pp_url_211
from utils.bkzj import get_bkzj1

import json
import pandas as pd

bp = Blueprint('other', __name__, url_prefix='/other')
#operate = Access()
#op = Sqlite('./utils/blog.db')
#data_new_db = Sqlite('./data/data_new.db')



# 静态文件路径
@bp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('../uploads/', filename)

@bp.route('/a_upph', methods=['GET', 'POST'])
def a_upph():
    try:
        u = assy_mes.UPPH_DAILY()
        if request.method == 'POST':
            # 从前端获取数据
            data = request.get_json()
            shift = data.get('shift', 'D')
            line = data.get('line', 'ASSY')
            station = data.get('station', 'STRU')
            employee = data.get('employee', 10)
            # 参数校验
            if not shift or not line or not station or not employee:
                return jsonify({"message": "Missing required parameters"})
            upph_data = u.upph(int(employee), line, shift, station)
            return jsonify({"status": "success", "data": upph_data})
            # return render_template("a_upph.html")
        return render_template('a_upph.html')
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

# 参数加密测试
@bp.route('/upph1', methods=['GET', 'POST'])
# @login_reguired
def upph1():
    if request.method == 'POST':
        encrypted_str = request.get_json().get('encrypted')
        # 处理前端加密数据
        aes = aes_decrypt()
        key = 'qazwsxedcrfvtgby'
        request_data = json.loads(aes.decrypt(
            encrypted=encrypted_str, key=key).decode())
        # print(request_data)
        try:
            data_hr = {
                'sub_hr': request_data.get('sub_hr'),
                'tnb_hr': request_data.get('tnb_hr'),
                'shift': request_data.get('shift')
            }
            # 获取upph并返回到前端页面
            upph = mes_n.upph(int(data_hr.get('sub_hr')), int(data_hr.get('tnb_hr')), shift=data_hr['shift'])
            # 每次更新页面前执行添加数据库动作，函数内部判断是否为指定时间
            # add_upph(upph)
            # 返回查询数据
            return jsonify(upph)
        except Exception as e:
            return jsonify({"code": 1, "data": {"message": str(e)}})
    # get请求为避免页面报错，发送初始数据填充
    data = mes_n.upph(1, 1, 'D')
    return render_template('upph1.html')

@bp.route('/upph2', methods=['GET', 'POST'])
# @login_reguired
def upph2():
    if request.method == 'POST':
        encrypted_str = request.get_json()
        # 处理前端加密数据
        try:
            data_hr = {
                'sub_hr': encrypted_str.get('sub_hr'),
                'tnb_hr': encrypted_str.get('tnb_hr'),
                'shift': encrypted_str.get('shift')
            }
            # 获取upph并返回到前端页面
            upph = mes_n.upph(int(data_hr.get('sub_hr')), int(data_hr.get('tnb_hr')), shift=data_hr['shift'])
            # 每次更新页面前执行添加数据库动作，函数内部判断是否为指定时间
            # add_upph(upph)
            # 返回查询数据
            return jsonify(upph)
        except Exception as e:
            return jsonify({"code": 1, "data": {"message": str(e)}})
    # get请求为避免页面报错，发送初始数据填充
    data = mes_n.upph(1, 1, 'D')
    return render_template('upph1.html', data=data)

@bp.route('/repair211/<line>/<shift>', methods=['get', 'post'])
def repair(line: str, shift: str) -> Response:
    try:
        today1 = str(datetime.datetime.today()).split(' ')[0]
        data = request.get_json().get('date')
        e_type = request.get_json().get('e_type')
        if data:
            today = data.replace('-', '/')
        else:
            today = today1.replace('-', '/')
        resp_data = mes211.main_request(today, line, shift, e_type)
        resp_data["input"] = mes_n.qcm_r(line, shift, today)
        if resp_data:
            return jsonify({"code": 1, "data": resp_data})
        else:
            return jsonify({"code": 0, "data": "后端获取数据出错，未查询到不良~稍后再试"})
    except Exception as e:
        return jsonify({"code": 0, "msg": f'获取数据出错，具体原因{str(e)}'})


@bp.route('/fail_qty', methods=['GET','POST'])
def fail_qty():
    """
    获取不良数量
    """
    if request.method == 'POST':
        line = request.get_json().get('line','')
        main_url = pp_url_211()[0]
        get_fail_qty(main_url)
        return jsonify(parse_fail_part('211.xls',line))  
    return render_template('fail.html')                 
@bp.route('/line_fail',methods=['POST'])
def fail_detail():
    """
    获取失败的详细信息
    """
    line=request.get_json().get('line','')
    df = pd.read_excel("D:/Program Files (x86)/web/211.xls", engine="xlrd")
    due_fail_groupby=df.groupby(["TEST_LINE",'ERROR_DESC'])["TEST_LINE"].count()
    line_fail_detail=df.loc[df['TEST_LINE']==line].groupby('ERROR_DESC')["TEST_LINE"].count().sort_values(ascending=False).to_json()
    return jsonify(json.loads(line_fail_detail))  

@bp.route('/gsa', methods=['GET', 'POST'])
def gsa():
    if request.method == 'POST':
        # arr = ['CN535100DD310075C03123957','3S12960129605C40900580N71J110','3S12960129605C40900580N71J110']
        arr = request.get_json().get('req_data')
        result = []
        for i in arr:
            result.append(get_data(i))
        return jsonify(result)
    return render_template('gsa.html')


@bp.route('/mpt', methods=['GET', 'POST'])
def mpt():
    if request.method == 'POST':
        process = request.args.get('p', '')
        if process.strip() == 'tnb':
            if datetime.datetime.now().hour<20 and datetime.datetime.now().hour>7:
                result = tnb_mpt('D')
            else:
                result = tnb_mpt('N')
        else:
            if datetime.datetime.now().hour<20 and datetime.datetime.now().hour>7:
                result = sub_mpt('D')
            else:
                result = sub_mpt('N')
        return jsonify(result)
    return render_template('mpt.html')

@bp.route('/checkStation', methods=['post','get'])
def checkStation():
    headers = {
        'Accept': 'text/html1,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': '10.128.128.120:9092',# 10.114.64.200
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    sn = request.values.get('sn')
    params_getstation = {
        'sn': sn,
        'CUSTOMER': 'A31',
        'SITE': 'CN53',
        'LINE': 'I3FA31SUBK',
        'GROUP': 'CSPT',
        'STATUS': 'PASS',
        'EC': '4H02',
        'udf2': 'STID',
        'udf3': 'PASS'
    }
    params_getbom = {
        'sn': sn,
        'CUSTOMER': 'A31',
        'SITE': 'CN53',
        'LINE': 'I3FA31SUBK',
        'GROUP': 'VIS',
        'udf2': 'QT',
        'udf3': 'GETBOM'
    }
    resp_getstation = requests.get(f'http://10.128.128.120:9092/FMDI/BASICVCI/BasicStationPass.ashx', headers=headers,
                                   params=params_getstation)
    resp_getbom = requests.get(f'http://10.128.128.120:9092/FMDI/BASICVCI/BasicGetInfo.ashx', headers=headers,
                               params=params_getbom)
    if resp_getstation.status_code == 200:
        return jsonify({'code': 1, 'data': {"station": resp_getstation.text, "bom": resp_getbom.text}})
    else:
        return jsonify({'code': 0, 'msg': '获取数据出错，请重试~'})

@bp.route('/getbom', methods=['get','post'])
def getbom():
    headers = {
        'Accept': 'text/html1,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,zh-CN;q=0.5',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Host': '10.128.128.120:9092',# 10.114.64.200
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.58'
    }
    sn = request.values.get('sn')
    # sn="8107827800469"
    params_getbom = {
        'sn': sn,
        'CUSTOMER': 'A31',
        'SITE': 'CN53',
        'LINE': 'I3FA31SUBK',
        'GROUP': 'VIS',
        'udf2': 'QT',
        'udf3': 'GETBOM'
    }
    resp_getbom = requests.get(f'http://10.128.128.120:9092/FMDI/BASICVCI/BasicGetInfo.ashx', headers=headers,
                               params=params_getbom)
    if resp_getbom.status_code == 200:
        # 1. 使用 XML 解析器获取根节点文本
        root = ET.fromstring(resp_getbom.text)
        content = root.text

        # 2. 使用正则从文本中提取具体值
        model = re.search(r'MODEL=(\S+)', content).group(1) if re.search(r'MODEL=(\S+)', content) else None
        sku = re.search(r'SKU=(\S+)', content).group(1) if re.search(r'SKU=(\S+)', content) else None
        return jsonify({"code": "1", "data": {"model":model, "sku":sku}})
    else:
        return jsonify({"code": 0, "msg": "获取数据出错，请重试~"})

@bp.route('/card', methods=['GET', 'POST'])
def card():
    if request.method == 'POST':
        card_no = request.get_json().get('card_no')
        linename = request.get_json().get('line_name')
        if linename.split('-')[1][:3]=='A31':
            area=linename.split('-')[1][:3]
        else:
            area=linename.split('-')[1][:6]
        if not card_no:
            return jsonify({"code": 0, "data": {"message": "工号不能为空！"}})
        card_result,username= card_record(card_no, area,linename)
        if card_result:
            return jsonify({"code": 1, "data": {"message": "刷卡OK!", "username": username,"area":area}})
        else:
            return jsonify({"code": 0, "data": {"message": "工号错误!", "username": username,"area":area}})
    return render_template('card.html')

@bp.route('/bkzj', methods=['GET', 'POST'])
def get_bkzj():
    if request.method == 'POST':
        day=request.get_json().get('d','d1')
        return jsonify(get_bkzj1(day))
    return render_template('socket.html')

if __name__ == '__main__':
    # data_list = api_obtm_list()[1:]
    # for data in data_list:
    #     print(data)
    # get_mi()
    # add_upph()
    # print(mes1.upph(10, 'SUB', shift='D'))
    # print(str(datetime.datetime.today()).split(' ')[0])
    # print(str(datetime.datetime.today()).split('-', 2)[1])
    pass
