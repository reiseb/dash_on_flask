from flask import Blueprint
from flask import redirect
from flask import render_template
from flask import request
from flask import url_for
from flask_login import current_user
from flask_login import login_required
from flask_login import login_user
from flask_login import logout_user
from werkzeug.urls import url_parse, url_join

from app.extensions import db
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.models import User

server_bp = Blueprint('main', __name__)


@server_bp.route('/')
def index():
    return render_template("index.html")


@server_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))

    form = LoginForm()
    if form.validate_on_submit():
        # escape form input
        username = str(form.username.data)
        password = str(form.password.data)

        # check credentials
        user = User.query.filter_by(username=username).first()
        if user is None or not user.check_password(password):
            error = 'Invalid username or password'
            return render_template('login.html', form=form, error=error)

        # log the user in
        login_user(user)

        # validate the next page request
        next_page = request.args.get('next')
        if not next_page or not _is_safe_redirect_url(next_page):
            next_page = url_for('main.index')

        # redirect
        return redirect(next_page)

    return render_template('login.html', form=form)


@server_bp.route('/logout/')
@login_required
def logout():
    logout_user()

    return redirect(url_for('main.index'))


@server_bp.route('/register/', methods=['GET', 'POST'])
@login_required
def register():
    if current_user.username == 'admin':
        form = RegistrationForm()
        if form.validate_on_submit():
            user = User(username=str(form.username.data))
            user.set_password(str(form.password.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('main.index'))
    else:
        return redirect(url_for('main.index'))

    return render_template('register.html', form=form)


def _is_safe_redirect_url(target):
    host_url = url_parse(request.host_url)
    redirect_url = url_parse(url_join(request.host_url, target))
    return (redirect_url.scheme in ('http', 'https') and
            host_url.netloc == redirect_url.netloc)
