# -*- coding: UTF-8 -*-
"""
Terms logic
"""
import simplejson as json

from application import application
from whatonearth.config import DATABACKEND as data_backend


def get_term(term):
    return data_backend.get(term)


def autocomplete_query(query):
    return data_backend.autocomplete(query)
