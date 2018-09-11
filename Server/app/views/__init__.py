from flask import render_template


class Router:
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        from app.views import code
        app.register_blueprint(code.api.blueprint)


def index():
    return render_template('index.html')
