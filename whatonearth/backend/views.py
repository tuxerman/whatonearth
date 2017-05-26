# -*- coding: UTF-8 -*-
"""
Frontend routes
"""
from flask import request
import simplejson as json

from application import application
from whatonearth.backend.term import autocomplete_query
from whatonearth.backend.term import get_term


@application.route('/term/autocomplete', methods=['GET'])
def search_terms():
    return json.dumps(autocomplete_query(request.args.get('query')))


@application.route('/term/<string:term>', methods=['GET'])
def fetch_term(term):
    return json.dumps(get_term(term))
