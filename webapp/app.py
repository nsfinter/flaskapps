from flask import Flask, current_app
from flask_debugtoolbar import DebugToolbarExtension
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_login import LoginManager
from webapp.config import config
import logging

# SQLAlchemyを生成する
db = SQLAlchemy()
# クロスサイトリクエストフォージェリを生成する
csrf = CSRFProtect()
# LoginManagerを生成する
login_manager = LoginManager()
# ログインしていないときにリダイレクトするエンドポイントを指定する
login_manager.login_view = "auth.login"
# ログイン後に表示するメッセージを指定する
# デフォルトで英語の文字が表示されるので、ここでは表示しない
login_manager.login_message = ""

def create_app(config_key):
    # flaskアプリを生成する
    app = Flask(__name__)
    # flaskアプリのコンフィグを設定する
    app.config.from_object(config[config_key])

    # flaskアプリのログレベルを設定する
    app.logger.setLevel(logging.DEBUG)
    # flaskアプリでデバッグツールバーを利用できるようにする
    toolbar = DebugToolbarExtension(app)

    # flaskアプリをSQLAlchemyに設定する
    db.init_app(app)
    # flaskアプリをMigrateに設定する
    Migrate(app, db)

    # flaskアプリにクロスサイトリクエストフォージェリを設定する
    csrf.init_app(app)

    # flaskアプリにLoginManagerを設定する
    login_manager.init_app(app)

    # mainteパッケージからviewsをimportする
    from webapp.mainte import views as maintes_views
    # flaskアプリにmainteブループリントオブジェクトを登録する
    app.register_blueprint(maintes_views.mainte, url_prefix="/mainte")

    # authパッケージからviewsをimportする
    from webapp.auth import views as auth_views
    # flaskアプリにauthブループリントオブジェクトを登録する
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # appliパッケージからviewsをimportする
    from webapp.appli import views as appli_views
    # flaskアプリにappliブループリントオブジェクトを登録する
    app.register_blueprint(appli_views.appli)

    return app
