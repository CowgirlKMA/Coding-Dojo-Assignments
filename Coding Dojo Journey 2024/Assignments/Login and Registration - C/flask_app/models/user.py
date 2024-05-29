from flask_app.config.mysqlconnection import connectToMySQL
#the (function)connectToMySQL lives  the (module)mysqlconnection.py file that's in the config folder that's in the flask_app folder
from flask import flash
from pprint import pprint

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 


class User:
    # setting attributes in a constructor function that accepts a dictionary as input
    def __init__(self, data):
        # accepting a dictionary as input, calling it data, take the values that are at the specific keys and use those values as the values for the object attribues
        # self.(what goes here are the columns from mySQL) this is the object attributes
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    @staticmethod
    def register_form_is_valid(form_data):
        #this method validates the registration form
        is_valid = True

        if len(form_data['first_name'].strip()) == 0:
            flash("Please enter first name.", "register")
            is_valid = False
        elif len(form_data['first_name'].strip()) < 2:
            flash("First name must be at least two characters.", "register")
            is_valid = False

        if len(form_data['last_name'].strip()) == 0:
            flash("Please enter last name.", "register")
            is_valid = False
        elif len(form_data['last_name'].strip()) < 2:
            flash("Last name must be at least two characters.", "register")
            is_valid = False

        if len(form_data['email'].strip()) == 0:
            flash("Please enter email.", "register")
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Email address is invalid.","register")
            is_valid = False

        if len(form_data['password'].strip()) == 0:
            flash("Please enter password.", "register")
            is_valid = False
        elif len(form_data['password'].strip()) < 8:
            flash("Password must be at least eight characters.", "register")
            is_valid = False

        elif form_data["password"] != form_data["confirm_password"]:
            flash("Passwords do not match.", "register")
            is_valid = False

        return is_valid


    @staticmethod
    def login_form_is_valid(form_data):
        #this method validates the login form
        is_valid = True

        if len(form_data['email'].strip()) == 0:
            flash("Please enter email.", "login")
            is_valid = False
        elif not EMAIL_REGEX.match(form_data['email']): 
            flash("Email address is invalid.","login")
            is_valid = False

        if len(form_data['password'].strip()) == 0:
            flash("Please enter password.", "login")
            is_valid = False
        elif len(form_data['password'].strip()) < 8:
            flash("Password must be at least eight characters.", "login")
            is_valid = False

        return is_valid 

    @classmethod
    def register(cls, user_data):
        #this method creates a new user into the database
        query = """
        INSERT INTO users
        (first_name, last_name, email, password)
        VALUES
        (%(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """

        user_id = connectToMySQL("login_and_registration").query_db(query, user_data)
        return user_id


    @classmethod
    def find_by_user_id(cls, user_id):
        #this method finds a user by user_id
        query = """SELECT * FROM users WHERE id = %(user_id)s;"""
        data = {"user_id": user_id}
        list_of_dicts = connectToMySQL("login_and_registration").query_db(query, data)
        if len(list_of_dicts) == 0:
            return None
        user = User(list_of_dicts[0])
        return user


    @classmethod
    def find_by_email(cls, email):
        #this method finds a user by email
        query = """SELECT * FROM users WHERE email = %(email)s;"""
        data = {"email": email}
        list_of_dicts = connectToMySQL("login_and_registration").query_db(query, data)
        if len(list_of_dicts) == 0:
            return None
        user = User(list_of_dicts[0])
        return user










# # creating class method to be able to do each CRUD query
#     @classmethod
#     def find_all(cls):
#         # find all users in the database
#         query = "SELECT * FROM users;"
#         # below users is the name of the schema, above users is the name of the table in that schema
#         list_of_dicts = connectToMySQL("users").query_db(query) 
#         # pprint(list_of_dicts)
#         users = []
#         for each_dict in list_of_dicts:
#             user = User(each_dict) # (to create a user) here users is calling the users constructer by passing in a data dictionary
#             users.append(user)
#         return users



#     @classmethod
#     def create(cls, form_data):
#     #inserts a new user into the database
#         query = """
#         INSERT INTO users
#         (first_name, last_name, email, password)
#         VALUES
#         (%(first_name)s, %(last_name)s, %(email)s, %(password));
#         """
#         connectToMySQL("users").query_db(query, form_data)



#     @classmethod
#     def find_by_id(cls, user_id):
#     #finds one user by their id in the database
#         query = "SELECT * FROM users WHERE id = %(user_id)s;"
#         data = {"user_id": user_id}
#         list_of_dicts = connectToMySQL("users").query_db(query, data)
#         # pprint(list_of_dicts)
#         print("user_id", user_id)
#         print("list_of_dicts", list_of_dicts)
#         # error handling
#         if len(list_of_dicts) == 0:
#             return None
#         user = User(list_of_dicts[0])
#         return user


#     @classmethod
#     def update(cls, form_data):
#     #updates the pet from the form that was submitted after editing
#         query = """
#         UPDATE users
#         SET
#         first_name=%(first_name)s, 
#         last_name=%(last_name)s, 
#         email=%(email)s
#         WHERE id = %(user_id)s;
#         """
#         connectToMySQL("users").query_db(query, form_data)
#         #calling this method implicitely returns none, this shows it explicitly
#         return 

#     @classmethod
#     def delete_by_id(cls, user_id):
#     #deletes user by the user id
#         query = "DELETE FROM users WHERE id = %(user_id)s;"
#         data = {"user_id": user_id}
#         connectToMySQL("users").query_db(query, data)
#         #calling this method implicitely returns none, this shows it explicitly
#         return 