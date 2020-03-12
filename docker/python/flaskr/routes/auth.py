from flask import (
    Blueprint, request, session,
    url_for, render_template, redirect,
    flash, current_app
)
from flaskr.tables.forms.auth import LoginForm


class Auth:

    bp = Blueprint('auth', __name__)

    @bp.route('/log-in', methods=['GET', 'POST'])
    def log_in():
        """
        Render the template to login and logs in a user.
        """
        form = LoginForm(request.form)
        if request.method == 'POST' and form.validate():
            if form.username.data != current_app.config['USERNAME']:
                flash('Invalid username.')
            elif form.password.data != current_app.config['PASSWORD']:
                flash('Invalid password.')
            else:
                session['logged_in'] = True
                flash('You were logged in.')

                return redirect(url_for('blog.show_posts'))

        return render_template('auth/log_in.html', form=form)

    @bp.route('/log-out')
    def log_out():
        """
        Log out a user.
        """
        session.pop('logged_in', None)
        flash('You were logged out.')

        return redirect(url_for('blog.show_posts'))
