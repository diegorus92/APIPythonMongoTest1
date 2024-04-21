from flask import Blueprint, jsonify, request
from ...BussinesLayer.services import TestService

testController = Blueprint("TestController", __name__)

@testController.route('/say-hello')
def say_hello():
    return TestService.say_hello()

@testController.route('/view-persons')
def view_persons():
    return jsonify({
                    "source_controller_file": "TestController.py",
                    "source_service_file": "TestService.py",
                    "data:": str(TestService.view_persons()),
                    })

@testController.route('/insert-person', methods=['POST'])
def insert_person():
    try:
        return str(TestService.insert_person())
    except Exception as ex:
        return f"Exception: {ex}"


