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

            
if __name__ == "__main__":
    app.run(debug=True)