# Import Necessary Libraries
from flask import Flask, render_template, request,redirect, session,url_for
from flask import Flask,jsonify,Markup, session, Response
import os
# Importing Blueprints defined in the routes -> adult_statistics.py
from routes.adult_statistics import adult_statistics_blueprint


app = Flask(__name__)


# Blueprints
app.register_blueprint(adult_statistics_blueprint)


if __name__ == "__main__":
    app_host = os.environ.get('APP_HOST') or '0.0.0.0'
    app_port = os.environ.get('APP_PORT') or 8001
    app.run(host=app_host, port=app_port, debug=False, threaded=True)
