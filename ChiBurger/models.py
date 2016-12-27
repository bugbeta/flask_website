# -*- coding: utf-8 -*-

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

from flask.ext.login import UserMixin
from . import db, login_manager

class User(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True, nullable=False, index=True)
    create_date = db.Column(db.Datetime)

    def __init__(self, username, password, email, create_date=None):
        self.username = username
        self.email = email
        if create_date is None:
            create_date = datetime.utcnow()
        self.create_date = create_date

        @property
        def password(self):
            raise AttributeError('password is not a readable attribute!')

        @password.setter
        def password(self, password):
            self.password_hash = generate_password_hash(password)

        def vertify_password(self, password):
            return check_password_hash(self.password_hash, password)

    # load user from session
    @login_manager.user_loader
    def login_user(user_id):
        return User.query.get(int(user_id))

    def __repr__(self):
        return '<User %r>' % self.username

