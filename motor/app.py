from flask import Flask
from flask_restful import Api
from vistas import VistaCandidatos

app = Flask(__name__)
app_context = app.app_context()
app_context.push()

api = Api(app)
api.add_resource(VistaCandidatos, '/candidatos')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)