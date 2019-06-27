from flask import Blueprint, render_template

app_bp = Blueprint('app', __name__, template_folder="templates", static_folder="static")


def init_app(app):
    app.register_blueprint(app_bp)

@app_bp.route('/')
def admin():
    return render_template("index.html")
