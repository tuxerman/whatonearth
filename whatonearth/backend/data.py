# -*- coding: UTF-8 -*-
"""
Frontend routes
"""
import yaml


class BaseDataBackend(object):
    """
    Implement a get function that fetches a key
    """
    def get(self, key):
        raise NotImplementedError

    def autocomplete(self, prefix):
        raise NotImplementedError


class SimpleYAMLBackend(BaseDataBackend):
    """
    An in-memory dict based on data read from a YAML file on disk
    """
    def __init__(self, yaml_filename):
        self._datastore = self._load_all_terms_from_yaml(yaml_filename)
        self._normed_keys = {
            self._norm(key): key
            for key in self._datastore.keys()
        }

    def _load_all_terms_from_yaml(self, yaml_filename):
        with open(yaml_filename, 'r') as handle:
            data = yaml.load(handle, Loader=yaml.Loader)
        return data

    def _norm(self, term):
        return term \
            .lower() \
            .replace('-', '') \
            .replace('_', '') \
            .replace(' ', '')

    def get(self, key):
        return self._datastore.get(key)

    def autocomplete(self, prefix):
        return [
            key
            for normed_key, key in self._normed_keys.items()
            if normed_key.startswith(self._norm(prefix))
        ]
