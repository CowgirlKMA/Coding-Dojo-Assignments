from flask_app import app
#flask_app lives in the __init__.py file, we are importing the app to this file
from flask_app.models.ninja import Ninja #Ninja is the name of the class
#all of the class methods live in the the ninja.py file, we are importing the entire file 
from flask_app.models.dojo import Dojo
from flask import render_template, redirect, request



@app.get("/ninjas/create")
#this route displays the new ninja form
def new_ninja():
    dojos = Dojo.find_all()
    return render_template("new_ninja.html", dojos=dojos)


@app.post("/ninjas/create")
#this route will process the form
def create_ninja():
    ninja_id = Ninja.create(request.form)
    dojo_id = request.form['dojo_id']
    return redirect(f"/dojos/{dojo_id}")

    
# @app.get("/ninjas/<int:ninja_id>")
# def ninja_details(ninja_id):
# #this route displays one ninja's details
#     ninja = Ninja.find_by_id_with_dojo(ninja_id)
#     # if ninja == None:
#     #     return "Cannot find ninja"
#     return render_template("ninja_details.html", ninja=ninja)


@app.get("/ninjas/<int:ninja_id>/edit")
def edit_ninja(ninja_id):
#this route displays the form to edit the ninja
    ninja = Ninja.find_by_id_with_dojos(ninja_id)

    return render_template("edit_ninja.html", ninja=ninja)


@app.post("/ninjas/update")
def update_ninja():
#this route processes the edit 
    Ninja.update(request.form) #passes from the form into the ninja.update
    return redirect("/dojos")

# @app.route("/ninjas")
# #this route displays all ninjas
# def all_ninjas():
#     ninjas = Ninja.find_all() # here ninja is the name of the class
#     return render_template("all_ninjas.html", ninjas=ninjas)
#     #ninjas=ninjas sends it to the template




    

# @app.post("/ninjas/<int:ninja_id>/delete")
# def delete_ninja(ninja_id):
# #this route will delete the ninja
#     Ninja.delete_by_id(ninja_id)
#     return redirect("/ninjas")