from flask import Flask, render_template, redirect, request, flash, url_for
from flask_login import LoginManager, login_user, login_required, current_user
from data import db_session
from data.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from UserLogin import UserLogin
import flask
from flask import jsonify

blueprint = flask.Blueprint(
    'courses_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/courses/<int:user_id>', methods=['GET'])
def get_news(user_id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == user_id).first()
    courses = str(user.courses).split(',')
    return jsonify(
        { 
            'courses':[ {} for i in courses]
        }
    )