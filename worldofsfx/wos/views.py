from flask import Blueprint, render_template

#: Specify each model defined in your models.py for each app here. This will
#: allow SQA to pick them up when the application is initialized
from worldofsfx.wos.models import *

wos = Blueprint('wos', __name__)


@wos.route('/')
def home():
    return render_template("wos/index.html")
