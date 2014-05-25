#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

#: Specify each model defined in your models.py for each app here. This will
#: allow SQA to pick them up when the application is initialized
from worldofsfx.events.models import *

beatport = Blueprint('beatport', __name__, url_prefix='/beatport')


@beatport.route('/')
def index():
    return render_template("beatport/index.html")
