# Import Necessary Libraries
from flask import Flask
from flask_cors import CORS


from utility.crud import execute_sql_file
from routes.adult_stats import adult_stats_blueprint

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# Blueprints
app.register_blueprint(adult_stats_blueprint)

if __name__ == "__main__":
    execute_sql_file()
    app_host = '0.0.0.0'
    app_port = 8002
    app.run(host=app_host, port=app_port, debug=False, threaded=True)
