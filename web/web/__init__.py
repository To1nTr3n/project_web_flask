import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_mail import Mail, Message
from flask_bootstrap import Bootstrap
from flask_moment import Moment

web = Flask(__name__)
web.config.from_object(Config)
db = SQLAlchemy(web)
migrate = Migrate(web, db)
login = LoginManager(web)
login.login_view = 'login'
bootstrap = Bootstrap(web)
moment = Moment(web)
mail = Mail(web)

if not web.debug:
    if web.config['MAIL_SERVER']:
        auth = None
        if web.config['MAIL_USERNAME'] or web.config['MAIL_PASSWORD']:
            auth = (web.config['MAIL_USERNAME'], web.config['MAIL_PASSWORD'])
        secure = None
        if web.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(web.config['MAIL_SERVER'], web.config['MAIL_PORT']),
            fromaddr='no-reply@' + web.config['MAIL_SERVER'],
            toaddrs=web.config['ADMINS'], subject='Myblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        web.logger.addHandler(mail_handler)

from web import routes, models, errors
