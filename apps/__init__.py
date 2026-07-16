# -*- coding: utf-8 -*-
"""
**************************************
*  @Author  ：   Joy_Lo
*  @Time    ：   2025/3/6 17:42
*  @Project :   flask_01
*  @FileName:   __init__.py.py
**************************************
程式用途:
"""
import os
from flask import Flask
from flask_cors import CORS
from apps.views import bp as index_bp
#from apps.views.image_view import bp as image_bp
#from apps.views.waive_view import bp as waive_bp
#from apps.views.borrow_view import bp as borrow_bp
#from apps.views.mb_view import bp as mb_bp
#from apps.views.efms_view import bp as efms_bp
#from apps.views.admin_view import bp as user_bp
#from apps.views.fixture_view import bp as fixture_bp
from apps.views.other_view import bp as other_bp
from apps.views.api_view import bp as api_bp
#from apps.views.api_model_img_info_view import bp as api_model_img_info_bp
#from apps.views.api_asset_view import bp as api_asset_bp
#from apps.views.api_mi_view import bp as api_mi_bp
#from apps.views.contact_view import bp as api_contact_bp
from settings import ProductionConfig
from flask_caching import Cache

os.environ['mes_username'] = 'gi\joy_lo'
os.environ['mes_password'] = 'compql123@'


def create_app():
    app = Flask(__name__, template_folder='../templates', static_folder='../static')
    CORS(app, resources=r'/*')
    app.config.from_object(ProductionConfig)
    app.secret_key = 'aswycbdjddjdueekejhb'
    app.config['PERMANENT_SESSION_LIFETIME'] = 60 * 60 * 12
    cache = Cache(app, config={'CACHE_TYPE': 'simple'})  # 可以使用其他类型的缓存，如Redis

    app.register_blueprint(index_bp)
    #app.register_blueprint(image_bp)
    #app.register_blueprint(waive_bp)
    #app.register_blueprint(borrow_bp)
    #app.register_blueprint(mb_bp)
    #app.register_blueprint(efms_bp)
    #app.register_blueprint(user_bp)
    #app.register_blueprint(fixture_bp)
    app.register_blueprint(other_bp)
    app.register_blueprint(api_bp)
    #app.register_blueprint(api_asset_bp)
    #app.register_blueprint(api_model_img_info_bp)
    #app.register_blueprint(api_mi_bp)
    #app.register_blueprint(api_contact_bp)

    # 配置文件上传目录
    UPLOAD_FOLDER = 'uploads'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    # 配置静态文件路径，使浏览器能访问上传的图片
    app.config['UPLOAD_URL'] = '../uploads'
    return app
