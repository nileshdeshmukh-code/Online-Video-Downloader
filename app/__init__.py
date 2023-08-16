from flask import Flask
app = Flask(__name__)
app.secret_key = "URL"

from app import routes
from app import error_handlers
