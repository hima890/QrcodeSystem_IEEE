from flask import Blueprint, render_template, request
from theFormForaccepted import db


errors = Blueprint('errors', __name__,
template_folder="templates",
static_folder="static")


@errors.app_errorhandler(404)
def error_404(error):
    return render_template('404.html'), 404


@errors.app_errorhandler(403)
def error_403(error):
    return render_template('403.html'), 403


@errors.app_errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
    