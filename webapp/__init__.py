from flask import Flask, flash, redirect, render_template, url_for
from flask_login import LoginManager

from webapp.db import db
from webapp.news.views import blueprint as news_blueprint
from webapp.user.models import User
from webapp.admin.views import blueprint as admin_blueprint
from webapp.user.views import blueprint as user_blueprint
from webapp.weather import weather_by_city


def create_app():
    app=Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(news_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    return app 