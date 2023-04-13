from flask import Flask, render_template, redirect, request, flash, url_for
from flask_login import LoginManager, login_user, login_required, current_user
from data import db_session
from data.users import User
from werkzeug.security import generate_password_hash, check_password_hash
from UserLogin import UserLogin


def get_name(id):
    db_sess = db_session.create_session()
    user = db_sess.query(User).filter(User.id == id).first()
    return user.name