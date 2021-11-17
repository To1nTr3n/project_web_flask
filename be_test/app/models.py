from datetime import datetime
from app import db,login, app
from werkzeug.security  import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import algorithms_available, md5
from time import time
import jwt


class User(UserMixin, db.Model):
    '''
        báo cho trình biên dịch Python biết cách 
        để in ra các thông tin về đối tượng
        => hữu dụng cho debugging 
    '''
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<User {}>'.format(self.username)
    
    # xử lí đăng nhập
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    '''
        u = User(username = 'toantran' , email= toan.187it23746@vanlanguni.vn)
        u.set_password('mypassword')
        u.check_password('mypassword')
        => True
        u.check_password('abc')
        => Flase
    '''

    def avatar(self, size):
        '''URL cho anh dai dien user'''
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

    # token
    def get_reset_password_toke(self, expried_in=600):
        return jwt.encode(
            {'reset_password': self.id, 'exp': time()+expried_in},
            app.config['SECRET_KEY'], algorithm='HS256').decode('utf-8')
    
    @staticmethod # phuong thuc tinh, goi truc tiep tu class chu khong phair khoi tao doi tuong moi
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithm =['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)


#hàm tai dữ liệu người dùng cho Flask-login
@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)





