from flask import Flask


# Initialize the app
application = Flask(__name__, instance_relative_config=True)
from . import views # Load the views

# Load the config file
application.config.from_object("config")
