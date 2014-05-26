from flask import Blueprint, render_template

#: Specify each model defined in your models.py for each app here. This will
#: allow SQA to pick them up when the application is initialized
from worldofsfx.buzz.models import *

buzz = Blueprint('buzz', __name__, url_prefix='/buzz')


@buzz.route('/')
def index():
    return render_template("buzz/index.html")
