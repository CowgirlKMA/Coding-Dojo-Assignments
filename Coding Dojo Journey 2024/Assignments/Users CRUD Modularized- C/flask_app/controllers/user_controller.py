from flask_app import app
#flask_app lives in the __init__.py file, we are importing the app to this file
from flask_app.models.user_model import User #User is the name of the class
#all of the class methods live in the the user_model.py file, we are importing the entire file 
from flask import render_template, redirect, request

@app.route("/")
@app.route("/users")
#this route displays all users
def index():
    users = User.find_all() # here user is the name of the class
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
    user_id = request.form["user_id"]
    
    User.update(request.form) #passes from the from into the user.update
    return redirect("/users")
    

@app.post("/users/<int:user_id>/delete")
def delete_user(user_id):
#this route will delete the user
    User.delete_by_id(user_id)
    return redirect("/")