#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Blueprint, render_template

#: Specify each model defined in your models.py for each app here. This will
#: allow SQA to pick them up when the application is initialized
from .models import *

mod = Blueprint('wos', __name__)


@mod.route('/')
def home():
    return render_template("wos/index.html")


@mod.route('/events')
def events():
    return render_template("wos/events.html")


@mod.route('/buzz')
def buzz():
    return render_template("wos/buzz.html")
