from flask import Flask

from . import views # Load the views

# Initialize the app
application = Flask(__name__, instance_relative_config=True)

# Load the config file
application.config.from_object("config")
