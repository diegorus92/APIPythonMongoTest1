from flask import request
from ...main import db

def say_hello():
    name = request.args.get("name")
    if name is None:
        return "Hello!"
    return f"Hello {name}!"

def view_persons():
    persons = list(db.persons.find())
    return persons

def insert_person():
    if len(request.args) == 5:
        result = db.persons.insert_one(
            {
                "name": request.args.get('name', type=str),
                "lastName": request.args.get('lastName', type=str),
                "address": request.args.get('address', type=str),
                "cellphone": request.args.get('cellphone', type=str),
                "age": request.args.get('age', type=int)
             }
        )
        return result
    raise Exception("No arguments found!")
