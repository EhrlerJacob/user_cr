from flask import Flask, render_template, redirect, request

from users import User

app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users():
    return render_template("index.html", users=User.get_all())

@app.route('/user/new')
def new_user():
    return render_template("create.html")

@app.route('/users/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def edit(id):
    data = {
        "id":id
    }
    return render_template("edit.html",user=User.get_user(data))

@app.route('/user/show/<int:id>')
def show(id):
    data = {
        "id":id
    }
    return render_template("user.html",user=User.get_user(data))

@app.route('/user/update', methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/deleteuser/<int:id>')
def deleteuser(id):
    data = {
        "id": id
    }
    User.deleteuser(data)
    return redirect('/users')


if __name__ == "__main__":
    app.run(debug=True, port=5000)
    