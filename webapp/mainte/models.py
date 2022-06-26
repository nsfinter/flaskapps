from datetime import datetime
from webapp.app import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    # テーブル名
    __tablename__ = "users"
    # カラム設定
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, index=True)
    email = db.Column(db.String, unique=True, index=True)
    password_hash = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    # パスワードのプロパティ
    @property
    def password(self):
        raise AttributeError("読み取り不可です。")
    
    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    # 入力したパスワードが正しいか判定する
    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

    # emailが重複しているか判定する
    def is_duplicate_email(self):
        return User.query.filter_by(email=self.email).first() is not None
