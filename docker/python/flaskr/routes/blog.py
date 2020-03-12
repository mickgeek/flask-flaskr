from flask import (
    Blueprint, request, session,
    url_for, abort, render_template,
    redirect, flash, current_app
)
from sqlalchemy.exc import StatementError
from flaskr.tables import database_schema
from flaskr.tables.database_engine import DatabaseEngine
from flaskr.tables.forms.blog import NewPostForm


class Blog:

    bp = Blueprint('blog', __name__)

    @bp.route('/')
    def show_posts():
        """
        Render the template to show posts.
        """
        db_session = DatabaseEngine(current_app).create_session()
        posts = db_session.query(database_schema.Post).all()

        return render_template('blog/show_posts.html', posts=posts)

    @bp.route('/add', methods=['GET', 'POST'])
    def add_post():
        """
        Add a post.
        """
        if not session.get('logged_in'):
            abort(401)

        form = NewPostForm(request.form)
        if request.method == 'POST' and form.validate():
            try:
                db_session = DatabaseEngine(current_app).create_session()
                post = database_schema.Post(title=request.form['title'], text=request.form['text'])
                db_session.add(post)
                db_session.commit()
                flash('The new post was successfully added.')

                return redirect(url_for('blog.show_posts'))
            except StatementError as exception:
                print('Database operation fails: ' + str(exception))

        return render_template('blog/add_post.html', form=form)
