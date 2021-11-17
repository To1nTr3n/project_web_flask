from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask_mail import Mail
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app) # đại diện CSDL 
migrate = Migrate(app, db) # đại diện thành phần chuyển đổi dữ liệu
mail = Mail(app)
bootstrap = Bootstrap(app)
login = LoginManager(app) #khởi tạo Flask-login
''' 4 yếu cầu của flask-login cho mô hình dữ liệu user
    is_authenticated: một thuộc tính sẽ được gán là True nếu user có tên và mật mã hợp lệ, False nếu một trong hai không đúng.
    is_active: một thuộc tính được gán là True nếu tài khoản user trong chế độ hoạt động (active) và False nếu ngược lại.
    is_anonymous: một thuộc tính được gán là False cho những user bình thường, và True cho những user ẩn danh (anonymous)
    get_id(): một phương thức để trả về định danh người dùng (id) dưới dạng chuỗi
'''
login.login_view = 'login' # yêu câu usef đăng nhập

# goi nhay kt bang email
# goi ERROR
# if not app.debug:
#     if app.config['MAIL_SERVER']:
#         auth = None
#         if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
#             auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
#         secure = None
#         if app.config['MAIL_USE_TLS']:
#             secure = ()
#         mail_handler = SMTPHandler(
#             mailhost= (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
#             fromaddr= 'no-reply@' +app.config['MAIL_SERVER'],
#             toaddrs= app.config['ADMINS'], subject= 'TN STORE Failure',
#             credentials= auth, secure = secure)
#         mail_handler.setLevel(logging.ERROR)
#         app.logger.addHandler(mail_handler) # kết nối thực thể này và đối tượng app.logger từ Flask

#     # ghi nhat ky vao file
#     if not os.path.exists('logs'):
#         os.mkdir('logs')
#     file_handler = RotatingFileHandler('logs/TNstore.log', maxBytes=10240, backupCount= 10 ) # backup 10 file du phong
#     file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s : %(message)s [in %(pathname)s:%(lineno)d]'))
#     # thời gian, cấp độ báo động (logging level), thông báo lỗi và tên của file mã nguồn gây ra lỗi và số dòng của lệnh đã gây ra lỗi trong flle đó
#     file_handler.setLevel(logging.INFO) # 5 cap do log tu thap den cao: DEBUG, INFO, WARNING, ERROR và CRITICA
#     app.logger.addHandler(file_handler)
#     app.logger.setLevel(logging.INFO)
#     app.logger.info('TNStore startup')

from app import routes, models, errors
