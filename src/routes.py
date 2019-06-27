from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__, template_folder="../templates/")


def init_app(app):
    app.register_blueprint(app_bp)


@app_bp.route('/')
def index():
    return "hello world"


@app_bp.route('/admin')
def admin():
    return render_template("index.html")
