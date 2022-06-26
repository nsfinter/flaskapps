from pathlib import Path

# アプリケーションルートのディレクトリ
rootdir = Path(__file__).parent.parent

class BaseConfig:
    # セッションを使えるようにする設定
    SECRET_KEY = "1qaz2wsx3edc4rfv5tgb6yhn7ujm"
    # デバッグツールバーでリダイレクトを許す設定
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class LocalConfig(BaseConfig):
    # データベースの設定
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{rootdir / 'local.sqlite'}"
    # 設定しないと警告が出るため設定している
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    # SQLをコンソールログに出力する設定
    SQLALCHEMY_ECHO=True

class TestingConfig(BaseConfig):
    # データベースの設定
    SQLALCHEMY_DATABASE_URI=f"sqlite:///{rootdir / 'testing.sqlite'}"
    # 設定しないと警告が出るため設定している
    SQLALCHEMY_TRACK_MODIFICATIONS=False

config = {
    "local": LocalConfig,
    "testing": TestingConfig,
}


