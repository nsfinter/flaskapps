from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email

class SingupForm(FlaskForm):
    username = StringField(
        "ユーザー名",
        validators=[
            DataRequired(message="ユーザー名を入力してください。"),
            Length(max=15, message="ユーザー名を15文字以内で入力してください。"),
        ]
    )
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired(message="メールアドレスを入力してください。"),
            Length(max=30, message="メールアドレスを30文字以内で入力してください。"),
            Email(message="メールアドレスが不正です。")
        ]
    )
    password = PasswordField(
        "パスワード",
        validators=[
            DataRequired(message="パスワードを入力してください。"),
            Length(max=15, message="パスワードを15文字以内で入力してください。"),
        ]
    )
    submit = SubmitField("新規登録")

class LoginForm(FlaskForm):
    email = StringField(
        "メールアドレス",
        validators=[
            DataRequired(message="メールアドレスを入力してください。"),
            Length(max=30, message="メールアドレスを30文字以内で入力してください。"),
        ]
    )
    password = PasswordField(
        "パスワード",
        validators=[
            DataRequired(message="パスワードを入力してください。"),
            Length(max=15, message="パスワードを15文字以内で入力してください。"),
        ]
    )
    submit = SubmitField("ログイン")