# -*- coding: UTF-8 -*-
"""
Configuration
"""
from whatonearth.backend.data import SimpleYAMLBackend

EXAMPLE_GLOSSARY = 'whatonearth/data/example_glossary.yaml'
DATABACKEND = SimpleYAMLBackend(EXAMPLE_GLOSSARY)
