from flask import Flask
from . import main as main_blueprint
from .AppLayer.Controllers.TestController import testController as testController_blueprint


def create_app():
    app = Flask(__name__)

    #Register of files .py with endpoints
    app.register_blueprint(main_blueprint.main)
    app.register_blueprint(testController_blueprint)

    return app


app = create_app()  #IMPORTANT