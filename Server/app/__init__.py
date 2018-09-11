from flask import Flask

from app.views import Router, index


def create_app(*config_cls):
    app_ = Flask(__name__, template_folder='../templates')

    for config in config_cls:
        app_.config.from_object(config)

    Router().init_app(app_)

    app_.add_url_rule('/', view_func=index)

    return app_

