# coding: utf-8
import sys
import site

sys.executable = '/usr/local/bin/python3.9'
print(sys.executable)
print(site.getsitepackages())

sys.path.insert(0, '/var/www/flask')

from app import app as application
