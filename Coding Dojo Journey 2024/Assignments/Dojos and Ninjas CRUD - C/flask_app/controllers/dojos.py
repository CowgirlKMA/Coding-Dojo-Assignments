from flask_app import app
#flask_app lives in the __init__.py file, we are importing the app to this file
from flask import render_template, redirect, request
from flask_app.models.dojo import Dojo #Dojo is the name of the class
#all of the class methods live in the the dojo.py file, we are importing the entire file 
from flask_app.models.ninja import Ninja

@app.route("/dojos")
#this route displays all dojos
def all_dojos():
    dojos = Dojo.find_all() # here dojo is the name of the class
    return render_template("all_dojos.html", dojos=dojos)
    #dojos=dojos sends it to the template


@app.get("/dojos")
#this route displays the new dojo form
def new_dojo():
    return render_template("all_dojos.html")


@app.post("/dojos/create")
#this route will process the form
def create_dojo():
    dojo_id = Dojo.create(request.form)
    return redirect("/dojos")


@app.get("/dojos/<int:dojo_id>")
def dojo_details(dojo_id):
#this route displays one dojo's details
    dojo = Dojo.find_by_id_with_ninjas(dojo_id)
    return render_template("dojo_details.html", dojo=dojo)


# @app.get("/dojos/<int:dojo_id>/edit")
# def edit_dojo(dojo_id):
# #this route displays the form to edit the dojo
#     dojo = Dojo.find_by_id(dojo_id)
#     if dojo == None:
#         return "Cannot find dojo"
#     return render_template("edit_dojo.html", dojo=dojo)


# @app.post("/dojos/update")
# def update_dojo():
# #this route processes the edit 
#     Dojo.update(request.form) #passes from the from into the dojo.update
#     return redirect("/dojos")
    

# @app.post("/dojos/<int:dojo_id>/delete")
# def delete_dojo(dojo_id):
# #this route will delete the dojo
#     Dojo.delete_by_id(dojo_id)
#     return redirect("/dojos")