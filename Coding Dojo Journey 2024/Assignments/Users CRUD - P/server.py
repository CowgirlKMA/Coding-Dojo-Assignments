from flask import Flask, render_template, redirect, request
from user_class_model import User # user: name of the file that defines the class, User: name of the class inside that file

app = Flask(__name__)

@app.route("/")
@app.route("/users")
#this route displays all users
def index():
    users = User.find_all() # here user is the class
    return render_template("index.html", users=users)
    #users=users sends it to the template


@app.get("/users/new")
#this route displays the new user form
def new_user():
    return render_template("new_user.html")


@app.post("/users/create")
#this route will process the form
def create_user():
    user_id = User.create(request.form)
    return redirect("/users")


@app.get("/users/<int:user_id>/show")
def user_details(user_id):
#this route displays one user's details
    user = User.find_by_id(user_id)
    if user == None:
        return "Cannot find user"
    return render_template("user_details.html", user=user)


@app.get("/users/<int:user_id>/edit")
def edit_user(user_id):
#this route displays the form to edit the user
    user = User.find_by_id(user_id)
    if user == None:
        return "Cannot find user"
    return render_template("edit_user.html", user=user)


@app.post("/users/update")
def update_user():
#this route processes the edit 
    User.update(request.form) #passes from the from into the user.update
    return redirect("/users")
    

@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
#this route will delete the user
    User.delete_by_id(user_id)
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
