from flask import Flask
from flask_restful import Api

from resources.rotas import *

app = Flask(__name__)
api = Api(app)


@app.route("/")
def landingpage():
    return 'oi'

api.add_resource(Cifra, '/encrypt/cifra')
api.add_resource(De_Cifra, '/decrypt/de_cifra')
api.add_resource(Enigma, '/encrypt/enigma')
api.add_resource(De_Enigma, '/decrypt/de_enigma')
api.add_resource(Para_OneHot, '/encrypt/one_hot') 
api.add_resource(Para_String, '/decrypt/string')

if __name__ == '__main__':
    app.run(debug=True)