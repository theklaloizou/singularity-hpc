__author__ = "Vanessa Sochat"
__copyright__ = "Copyright 2021, Vanessa Sochat"
__license__ = "MPL 2.0"


environment_file = """#!/bin/sh

# Add custom environment variables here with export
{% for key, value in envars.items() %}export {{ key }}="{{ value }}"
{% endfor %}
"""
