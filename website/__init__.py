# makes website folder  a python package


from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'HAYARAN'

    from .views import views #importing views blueprint
    from .auth import auth

    app.register_blueprint(views,url_prefix = '/')
    app.register_blueprint(auth,url_prefix = '/') # no prefix

    return app