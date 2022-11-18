from flask import Flask

app=Flask(__name__)

app.config["SECRET_KEY"]="YouCantSeEmeE"
from phonebook_flask import routes
