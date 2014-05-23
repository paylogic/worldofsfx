#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

#: Specify each model defined in your models.py for each app here. This will
#: allow SQA to pick them up when the application is initialized
from worldofsfx.events.models import *

events = Blueprint('events', __name__, url_prefix='/events')


@events.route('/')
def index():
    return render_template("events/index.html")
