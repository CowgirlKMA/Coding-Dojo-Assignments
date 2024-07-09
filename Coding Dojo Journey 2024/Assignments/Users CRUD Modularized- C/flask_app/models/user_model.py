from flask_app.config.mysqlconnection import connectToMySQL
#the (function)connectToMySQL lives in the (module)mysqlconnection.py file that's in the config folder that's in the flask_app folder
from pprint import pprint


class User:

    # setting attributes in a constructor function that accepts a dictionary as input
    def __init__(self, data):
        # accepting a dictionary as input, calling it data, take the values that are at the specific keys and use those values as the values for the object attribues
        # self.(what goes here are the columns from mySQL) this is the object attributes
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


# creating class method to be able to do each CRUD query
    @classmethod
    def find_all(cls):
        # find all users in the database
        query = "SELECT * FROM users;"
        # below users is the name of the schema, above users is the name of the table in that schema
        list_of_dicts = connectToMySQL("users").query_db(query) 
        # pprint(list_of_dicts)
        users = []
        for each_dict in list_of_dicts:
            user = User(each_dict) # (to create a user) here users is calling the users constructer by passing in a data dictionary
            users.append(user)
        return users
    

    @classmethod
    def create(cls, form_data):
    #inserts a new user into the database
        query = """
        INSERT INTO users
        (first_name, last_name, email)
        VALUES
        (%(first_name)s, %(last_name)s, %(email)s);
        """
        connectToMySQL("users").query_db(query, form_data)



    @classmethod
    def find_by_id(cls, user_id):
    #finds one user by their id in the database
        query = "SELECT * FROM users WHERE id = %(user_id)s;"
        data = {"user_id": user_id}
        list_of_dicts = connectToMySQL("users").query_db(query, data)
        # pprint(list_of_dicts)
        print("user_id", user_id)
        print("list_of_dicts", list_of_dicts)
        # error handling
        if len(list_of_dicts) == 0:
            return None
        user = User(list_of_dicts[0])
        return user


    @classmethod
    def update(cls, form_data):
    #updates the user from the form that was submitted after editing
        query = """
        UPDATE users
        SET
        first_name=%(first_name)s, 
        last_name=%(last_name)s, 
        email=%(email)s
        WHERE id = %(user_id)s;
        """
        connectToMySQL("users").query_db(query, form_data)
        #calling this method implicitely returns none, this shows it explicitly
        return 

    @classmethod
    def delete_by_id(cls, user_id):
    #deletes user by the user id
        query = "DELETE FROM users WHERE id = %(user_id)s;"
        data = {"user_id": user_id}
        connectToMySQL("users").query_db(query, data)
        #calling this method implicitely returns none, this shows it explicitly
        return 