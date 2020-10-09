from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()
from models import Student


def create_app():
    app = Flask(__name__, template_folder='templates')
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    # index route
    @app.route('/')
    def index():
        student = Student.query.all()
        return render_template('index.html', student=student)

    # register route
    @app.route('/register/', methods=['GET', 'POST'])
    def register():
        if request.method == 'POST':
            student = Student(
                request.form['student_name'], request.form['student_age'], request.form['student_email']
            )
            db.session.add(student)
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('register.html')

    # editing route
    @app.route('/edit/<int:id>/', methods=['GET', 'POST'])
    def edit(id):
        student = Student.query.get(id)
        if request.method == 'POST':
            student.name = request.form['student_name']
            student.age = request.form['student_age']
            student.email = request.form['student_email']
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('edit.html', student=student)

    # delete route
    @app.route('/delete/<int:id>/', methods=['GET', 'POST'])
    def delete(id):
        student = Student.query.get(id)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('index'))

    return app
