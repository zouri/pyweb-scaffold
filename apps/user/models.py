# -*- coding:utf-8 -*-
#
# Created Time: 2020/4/16 5:49 下午
# Be From: ZouRi
# Last Modified: x
# e6b0b8e8bf9ce5b9b4e8bdbbefbc8ce6b0b8e8bf9ce783ade6b3aae79b88e79cb6
#
from uuid import uuid1
from datetime import datetime
from apps.main import db, flask_bcrypt


class User(db.Model):
    """ 用户表
    """
    __tablename__ = "user"

    uid = db.Column(db.String(100), primary_key=True, default=uuid1().hex)
    username = db.Column(db.String(100), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.String(100))
    role = db.Column(db.String(100), default='user')
    registration_time = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Integer, default=0, nullable=False)

    @property
    def password(self):
        raise AttributeError('password: write-only field')

    @password.setter
    def password(self, password):
        self.password_hash = flask_bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return flask_bcrypt.check_password_hash(self.password_hash, password)

    def to_json(self):
        registration_time = self.registration_time.strftime("%Y-%m-%d %H:%S:%M") if self.registration_time else ''
        return {
            'uid': self.uid,
            'username': self.username,
            'email': self.email,
            'role': self.role,
            'registration_time': registration_time,
            'status': self.status,
            'avatar': '',
        }

    def __repr__(self):
        return f"<User '{self.username}'>"
