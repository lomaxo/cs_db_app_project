from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from cs_db_app.auth import login_required
from cs_db_app.db import get_db

bp = Blueprint('inventory', __name__)

@bp.route('/')
def list():
    db = get_db()
    items = db.execute(
        'SELECT description, location_id'
        ' FROM item'
        ' ORDER BY location_id'
    ).fetchall()
    return render_template('inventory/list.html', items=items)


@bp.route('/add', methods=('GET', 'POST'))
@login_required
def add():
    if request.method == 'POST':
        description = request.form['description']
        location = request.form['location']
        error = None

        if not description:
            error = 'Description is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO item (description, location_id)'
                ' VALUES (?, ?)',
                (description, location)
            )
            db.commit()
            return redirect(url_for('inventory.list'))

    return render_template('inventory/add.html')