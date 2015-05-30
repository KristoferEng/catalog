activate_this = '/var/www/html/catalog/project.py'
execfile(activate_this, dict(__file__=activate_this))

from project import app as application

import sys
sys.stdout = sys.stderr