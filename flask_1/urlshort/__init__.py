from flask import Flask

def create_app(test_config=None):
    app = Flask(__name__)
    app.secret_key = 'hk12k3khhkh23k123k13kh1k231h23h123k'

    from . import urlshort
    app.register_blueprint(urlshort.bp)

    return app