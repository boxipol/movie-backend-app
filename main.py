from flask import Flask
from movies.movies_api import movies_api

app = Flask(__name__)
app.register_blueprint(movies_api)
