# -*- coding: UTF-8 -*-
"""
Whatonearth application
"""
import os
from flask import Flask

APP_ROOT = os.path.dirname(os.path.realpath(__file__))
application = Flask(__name__)

from whatonearth.frontend.views import *
from whatonearth.backend.views import *

if __name__ == '__main__':
    application.run(host='0.0.0.0')
