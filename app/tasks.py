from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort
from app.database import db
from app.models import Task

bp = Blueprint('tasks', __name__)

@bp.route('/')
def index():
    tasks = Task.query.all()
    return render_template('tasks/index.html', tasks=tasks)

@bp.route('/tasks/create')
def create():
    return render_template('tasks/create.html')

@bp.route('/tasks', methods=['POST'])
def store():
    task = Task()
    task.title = request.form['title']
    task.memo = request.form['memo']
    db.session.add(task)
    db.session.commit()
    flash('create new task.')
    return redirect(url_for('tasks.index'))

@bp.route('/tasks/<int:id>')
def show(id):
    task = Task.query.filter_by(id=id).first_or_404()
    return render_template('tasks/show.html', task=task)

@bp.route('/tasks/<int:id>/edit')
def edit(id):
    task = Task.query.filter_by(id=id).first_or_404()
    return render_template('tasks/edit.html', task=task)

@bp.route('/tasks/<int:id>/update', methods=['POST'])
def update(id):
    task = Task.query.filter_by(id=id).first()
    task.title = request.form['title']
    task.memo = request.form['memo']
    db.session.add(task)
    db.session.commit()
    flash('updated task.')
    return redirect(url_for('tasks.show', id=task.id))

@bp.route('/tasks/<int:id>/delete', methods=['POST'])
def destroy(id):
    task = Task.query.get(id)
    db.session.delete(task)
    db.session.commit()
    flash('deleted task.')
    return redirect(url_for('tasks.index'))