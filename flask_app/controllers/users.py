from flask_app import app
from flask_app.models.user import User

from flask import render_template, redirect, session, request


@app.route('/')
def index():
    users=User.get_all()
    return render_template('read.html', users=users)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/create/user', methods=['POST'])
def createUser():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email_address'],
    }
    user_id = User.create(data)
    return redirect('/show/' + str(user_id['id']))

@app.route('/show/<int:id>')
def showUser(id):
    data = {
        'id': id
    }
    user=User.get_user_by_id(data)
    return render_template('show.html', user=user)


@app.route('/delete/<int:id>')
def deleteUser(id):
    data = {
        'id': id
    }
    User.delete(data)
    return redirect('/')



@app.route('/edit/<int:id>')
def editUser(id):
    data = {
        'id': id
    }
    user=User.get_user_by_id(data)
    return render_template('edit.html', user=user)

@app.route('/update/<int:id>', methods=['POST'])
def updateUser(id):
    data = {
        'id': id
    }
    User.update(data)
    return redirect('/show/' + str(id))