import os

from flask import Flask, render_template
from flaskr.routes.auth import Auth
from flaskr.routes.blog import Blog
from flaskr.tables.database_engine import DatabaseEngine


def render_unauthorized_page(error):
    """
    Render the error page.
    """
    return render_template('error_401.html', error=error), 401

def render_not_found_page(error):
    """
    Render the error page.
    """
    return render_template('error_404.html', error=error), 404

def create_app():
    """
    Initialize the application, database and register additional functions.
    """
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(os.path.join(app.root_path, 'config.py'))

    if app.config['TESTING']:
        app.config.update(dict(
            SQLALCHEMY_DATABASE_URI=app.config['TEST_DATABASE_URI'],
        ))

    app.register_error_handler(401, render_unauthorized_page)
    app.register_error_handler(404, render_not_found_page)

    DatabaseEngine(app).init_app()

    app.register_blueprint(Auth.bp)
    app.register_blueprint(Blog.bp)

    return app
