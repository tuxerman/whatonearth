# -*- coding: UTF-8 -*-
"""
Frontend routes
"""
from application import application
from flask import render_template


@application.route('/', methods=['GET'])
def www_show_home():
    return render_template(
        'home.html'
    )
