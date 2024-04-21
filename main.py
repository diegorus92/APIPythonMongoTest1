from flask import Blueprint
from .DataLayer.Data.database import Database


main = Blueprint("main", __name__)

_database = Database() #start connection with MongoCLient and get 'contacts' database
db = _database.get_database_context() #get acces to collections in database
                                      #Any other .py file only need to import this object to use it and
                                      #manipulate database collections

@main.route('/')
def greetings():
    return "Welcome to my API"

@main.route('/persons')
def view_persons():
    print(list(db.persons.find()))
    return f"From main.py --> {str(list(db.persons.find()))}"
