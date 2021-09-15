#!/usr/bin/python
from webApp import app as application
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, ”/ var/www/webApp /“)

application.secret_key = ‘my secret key’
