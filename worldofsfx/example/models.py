#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    An example models.py for use with worldofsfx

    Useage::

        from worldofsfx.database import db

        class FooModel(db.Model):

            __tablename__ = 'foos'

            id = db.Column(db.Integer, primary=True)
            name = db.Column(db.String(30), nullable=False)
"""

from worldofsfx.database import db
