"""
Settings for the application
"""
import os

if os.getenv("DEBUG", "false").lower() == "true":
    DEBUG = True
else:
    DEBUG = False
