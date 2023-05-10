from flask import Flask
from website.Controller import routes
import sys
import os
sys.path.insert(0, '../website')
#from website.Controller import routes


def create_app():
    tempDir = os.path.abspath('website/View/templates')
    staticDir = os.path.abspath('website/View/static')
    app = Flask(__name__, template_folder=tempDir, static_folder=staticDir) # override template / static location (MVC)
    app.config['SECRET_KEY'] = 'boeing' # encrypts the data for our website (cookies, etc.)

    # Before it can access the decorator location it goes
    # through here first (example, if it was /route, and the original was home,
    # then it would be /route/home)
    app.register_blueprint(routes.routes, url_prefix='/') 

    return app
    