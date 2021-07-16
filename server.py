from flask import Flask, render_template, request, redirect, url_for

from users import Users
app = Flask(__name__)
@app.route("/users/create")
def index():
    return render_template("index.html")

@app.route('/create_user', methods=["POST"])
def create_user():
    
    data = {
        "fname": request.form["fname"],
        "lname" : request.form["lname"],
        "email" : request.form["email"]
    }
    
    Users.save(data)
    
    return redirect('/users')


@app.route('/users')
def readAll():
    return render_template('read.html', users=Users.get_all())

@app.route('/users/<id>')
def showUser(id):
    return render_template( 'show.html', user=Users.get(id))

@app.route("/users/<id>/edit")
def edit(id):
    return render_template("edit.html", user=Users.get(id))

@app.route("/users/<id>/update", methods=["POST"])
def update(id):
    data = {
        "first_name": request.form["fname"],
        "last_name" : request.form["lname"],
        "email" : request.form["email"],
        'id': id
    }
    print(data["first_name"])
    Users.setUser(data) 
    return redirect('/users/%s'%(id))

@app.route('/users/<id>/delete')
def deleteUser(id):
    data ={
        'id': id
    }
    Users.deleteUser(data)
    return redirect('/users')



            
if __name__ == "__main__":
    app.run(debug=True)