from flask import Flask, render_template
from app.database import init_db

def page_not_found(e):
    return render_template('404.html'), 404

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    init_db(app)

    from . import tasks
    app.register_blueprint(tasks.bp)
    app.add_url_rule('/', endpoint='index')
    
    app.register_error_handler(404, page_not_found)

    return app;