from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja
from pprint import pprint


class Dojo:

    # setting attributes in a constructor function that accepts a dictionary as input
    def __init__(self, data):
        # accepting a dictionary as input, calling it data, take the values that are at the specific keys and use those values as the values for the object attribues
        # self.(what goes here are the columns from mySQL) this is the object attributes
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []#dojos is the parent, ninjas are the child we are able to populate this list with the info the info from find_by_id_with_ninjas 


# creating class method to be able to do each CRUD query
    @classmethod
    def find_all(cls):
        # find all dojos in the database
        query = "SELECT * FROM dojos;"
        # below dojos_and_ninjas.db is the name of the schema, above dojos is the name of the table in that schema
        list_of_dicts = connectToMySQL("dojos_and_ninjas.db").query_db(query) 
        pprint(list_of_dicts)
        dojos = []
        for each_dict in list_of_dicts:
            dojo = Dojo(each_dict) # (to create a dojo) here dojo is calling the dojos constructer by passing in a data dictionary
            dojos.append(dojo)
        return dojos
    

    @classmethod
    def find_by_id_with_ninjas(cls, dojo_id):
        #finds one dojo by id and related child ninjas in the database
        # left join gives you all dojos and ninjas if there are any
        query = """
        SELECT * FROM dojos 
        LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id
        WHERE dojos.id = %(dojo_id)s;
        """
        data = {"dojo_id": dojo_id}
        list_of_dicts = connectToMySQL("dojos_and_ninjas.db").query_db(query, data)
        #when we get this list of dictionaries we are changing them into objects, this is object oriented programming, we are building an object-relational mapping ORM from the ground up; taking database information and turning them into , we are mapping our columns from the database into attributes of an object- see def__init__(self, data)above
        pprint(list_of_dicts)
        dojo = Dojo(list_of_dicts[0])#instantiated object
        print(dojo.name)
        for each_dict in list_of_dicts:
            ninja_data = {
                "id": each_dict['ninjas.id'],
                "first_name": each_dict['first_name'],
                "last_name": each_dict['last_name'],
                "age": each_dict['age'],
                "dojo_id": each_dict['dojo_id'],
                "created_at": each_dict['ninjas.created_at'],                   
                "updated_at": each_dict['ninjas.updated_at'],
                }
            ninja = Ninja(ninja_data)#instatiated object
            dojo.ninjas.append(ninja)
        return dojo



    @classmethod
    def create(cls, form_data):
    #inserts a new dojos into the database
        query = """
        INSERT INTO dojos
        (name)
        VALUES
        (%(name)s);
        """
        connectToMySQL("dojos_and_ninjas.db").query_db(query, form_data)



    @classmethod
    def find_by_id(cls, dojo_id):
    #finds one dojos by their id in the database
        query = "SELECT * FROM dojos WHERE id = %(dojo_id)s;"
        data = {"dojo_id": dojo_id}
        list_of_dicts = connectToMySQL("dojos_and_ninjas.db").query_db(query, data)
        pprint(list_of_dicts)
        print("dojo_id", dojo_id)
        print("list_of_dicts", list_of_dicts)
        # error handling
        if len(list_of_dicts) == 0:
            return None
        dojo = Dojo(list_of_dicts[0])
        return dojo


    # @classmethod
    # def update(cls, form_data):
    # #updates the dojo from the form that was submitted after editing
    #     query = """
    #     UPDATE dojos
    #     SET
    #     name=%(name)s 
    #     WHERE id = %(dojo_id)s;
    #     """
    #     connectToMySQL("dojos_and_ninjas.db").query_db(query, form_data)
    #     #calling this method implicitely returns none, this shows it explicitly
    #     return 


    # @classmethod
    # def delete_by_id(cls, dojo_id):
    # #deletes dojos by the dojos id
    #     query = "DELETE FROM dojos WHERE id = %(dojo_id)s;"
    #     data = {"dojo_id": dojo_id}
    #     connectToMySQL("dojos_and_ninjas.db").query_db(query, data)
    #     #calling this method implicitely returns none, this shows it explicitly
    #     return 