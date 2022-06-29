from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, Email

class UserForm(FlaskForm):
    username = StringField(
        label="ユーザー名",  
        validators=[
            DataRequired(message="ユーザー名を入力してください。"), 
            Length(max=15, message="ユーザー名を15文字以内で入力してください。"),
        ]
    )
        
    email = StringField(
        label="メールアドレス",
        validators=[
            DataRequired(message="メールアドレスを入力してください。"),
            Length(max=30, message="メールアドレスを30文字以内で入力してください。"),
            Email(message="メールアドレスが不正です。"),
        ]
    )

    password = PasswordField(
        label="パスワード",
        validators=[
            DataRequired(message="パスワードを入力してください。"),
            Length(max=15, message="パスワードを15文字以内で入力してください。"),
        ]
    )

    submit = SubmitField(
        label="新規登録"
    )