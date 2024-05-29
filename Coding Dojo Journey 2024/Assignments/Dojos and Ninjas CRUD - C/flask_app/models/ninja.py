from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo
from pprint import pprint


class Ninja:
    # setting attributes in a constructor function that accepts a dictionary as input
    def __init__(self, data):
        # accepting a dictionary as input, calling it data, take the values that are at the specific keys and use those values as the values for the object attribues
        # self.(what goes here are the columns from mySQL) this is the object attributes
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojo_id = data["dojo_id"]
        self.create_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.myth = []


# creating class method to be able to do each CRUD query
    @classmethod
    def find_by_id(cls, ninja_id):
    #finds one ninja by their id in the database
        query = "SELECT * FROM ninjas WHERE id = %(ninja_id)s;"
        data = {"ninja_id": ninja_id}
        list_of_dicts = connectToMySQL("dojos_and_ninjas.db").query_db(query, data)
        # pprint(list_of_dicts)
        print("ninja_id", ninja_id)
        print("list_of_dicts", list_of_dicts)
        # error handling
        if len(list_of_dicts) == 0:
            return None
        ninja = Ninja(list_of_dicts[0])
        return ninja


    @classmethod
    def find_by_id_with_dojos(cls, ninja_id):
    #finds one ninja by their id and it's dojo in the database
        query = """
        SELECT * FROM  ninjas
        LEFT JOIN dojos
        ON  dojos.id = ninjas.dojo_id
        WHERE ninjas.id = %(ninja_id)s;
        """

        data = {"ninja_id": ninja_id}
        list_of_dicts = connectToMySQL("dojos_and_ninjas.db").query_db(query, data)
        pprint(list_of_dicts)

        ninja = Ninja(list_of_dicts[0])
        dojo_data = {
            "id": list_of_dicts[0]['dojos.id'],
            "name": list_of_dicts[0]['name'],
            "created_at": list_of_dicts[0]['dojos.created_at'],
            "updated_at": list_of_dicts[0]['dojos.updated_at'],
        }
        dojo_parent = dojo.Dojo(dojo_data)
        ninja.dojo = dojo_parent

        return ninja  

    @classmethod
    def create(cls, form_data):
    #inserts a new ninja into the database
        query = """
        INSERT INTO ninjas
        (first_name, last_name, age, dojo_id)
        VALUES
        (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s);
        """
        ninja_id = connectToMySQL("dojos_and_ninjas.db").query_db(query, form_data)
        return ninja_id


    @classmethod
    def update(cls, form_data):
    #updates the ninja from the form that was submitted after editing
        query = """
        UPDATE ninjas
        SET
        first_name=%(first_name)s, 
        last_name=%(last_name)s, 
        age=%(age)s,
        dojo_id=%(dojo_id)s,
        WHERE id = %(ninja_id)s;
        """
        connectToMySQL("dojos_and_ninjas.db").query_db(query, form_data)
        #calling this method implicitely returns none, this shows it explicitly
        return 

        
    # @classmethod
    # def find_all(cls):
    #     # find all ninjas in the database
    #     query = "SELECT * FROM ninjas;"
    #     # below ninjas is the name of the schema, above ninjas is the name of the table in that schema
    #     list_of_dicts = connectToMySQL("dojos_and_ninjas.db").query_db(query) 
    #     pprint(list_of_dicts)
    #     ninjas = []
    #     for each_dict in list_of_dicts:
    #         ninja = Ninja(each_dict) # (to create a ninja) here ninjas is calling the ninjas constructer by passing in a data dictionary
    #         ninjas.append(ninja)
    #     return ninjas






    # @classmethod
    # def delete_by_id(cls, ninja_id):
    # #deletes ninja by the ninja id
    #     query = "DELETE FROM ninjas WHERE id = %(ninja_id)s;"
    #     data = {"ninja_id": ninja_id}
    #     connectToMySQL("dojos_and_ninjas.db").query_db(query, data)
    #     #calling this method implicitely returns none, this shows it explicitly
    #     return 