from flask import Blueprint, current_app, render_template, redirect, url_for
from webapp.app import db
from webapp.mainte.models import User
from webapp.mainte.forms import UserForm

mainte = Blueprint("mainte", __name__, template_folder="templates", static_folder="static")

@mainte.route("/")
def index():
    # ログを出力する
    current_app.logger.debug("mainte.index start")
    return render_template("mainte/index.html")

# ユーザー一覧画面
@mainte.route("/users/")
def users_index():
    # ログを出力する
    current_app.logger.debug("mainte.users start")
    users = User.query.all()
    return render_template("mainte/users/index.html", users=users)

# ユーザー新規登録画面
@mainte.route("/users/create", methods=["GET", "POST"])
def users_create():
    form = UserForm()
    if form.validate_on_submit():
        user = User(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("mainte.users_index"))
    return render_template("mainte/users/create.html", form=form)

# ユーザー更新画面
@mainte.route("/users/<user_id>", methods=["GET", "POST"])
def users_update(user_id):
    form = UserForm()
    # ユーザー情報をDBから取得
    user = User.query.filter_by(id=user_id).first()

    if form.validate_on_submit():
        user.username = form.username.data
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("mainte.users_index"))
    return render_template("mainte/users/update.html", form=form, user=user)

# ユーザー削除機能
@mainte.route("/users/<user_id>/delete", methods=["GET"])
def users_delete(user_id):
    user = User.query.filter_by(id=user_id).first()
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for("mainte.users_index"))