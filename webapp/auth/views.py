from flask import Blueprint, render_template, flash, url_for, redirect, request
from webapp.auth.forms import SingupForm, LoginForm
from webapp.mainte.models import User
from webapp.app import db
from flask_login import login_user, logout_user

auth = Blueprint("auth", __name__, template_folder="templates", static_folder="static")

@auth.route("/signup", methods=["GET", "POST"])
def signup():
    form = SingupForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )

        # メールアドレス重複チェック
        if user.is_duplicate_email():
            flash("指定のメールアドレスは登録済みです。")
            return redirect(url_for("auth.signup"))
        
        # ユーザー情報を登録する
        db.session.add(user)
        db.session.commit()
        # ユーザー情報をセッションに設定する
        login_user(user)
        # GETパラメータにnextキーが存在し、値がない場合はindexへリダイレクト
        next_ = request.args.get("next")
        if next_ is None or not next_.startswith("/"):
            next_ = url_for("mainte.index")
        return redirect(next_)
    
    return render_template("auth/signup.html", form=form)

@auth.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # ユーザーが存在しパスワードが一致した場合はログインを許可する
        if user is not None and user.verify_password(form.password.data):
            login_user(user)
            return redirect(url_for("mainte.index"))
        
        # ログイン失敗のメッセージを設定する
        flash("メールアドレスかパスワードが不正です。")
    
    return render_template("auth/login.html", form=form)

@auth.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
