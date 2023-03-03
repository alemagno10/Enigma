from flask import Flask, render_template, make_response, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from pathlib import Path
from model.sql_alchemy_para_db import db
from resources.rotas import Desafios, PararSeguir, Segue, SeguidoPor, Usuario, Login, Logout, Tags, ListarDesafios, ListarUsuarios, ListarTags, DesafioTag, Seguir, Cadastro, DesafiosUsuario, TopCriadores, Ranking, Acertou, ListaDesafiosUsuario, UsuarioPontos
from flask_httpauth import HTTPBasicAuth
from flask_bcrypt import Bcrypt
from model.modelos import *
from model.forms import LoginForm, CadastroForm
from flask_cors import CORS

# Resistente a sistema operacional
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
# caminho para a base
rel_arquivo_db = Path('model/base_de_dados.db')
caminho_arq_db = src_folder / rel_arquivo_db


app = Flask(__name__)
CORS(app)
#https://docs.sqlalchemy.org/en/14/core/engines.html
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{caminho_arq_db.resolve()}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'toadcode'
api = Api(app)


@app.route("/")
def landingpage():
    return 'oi'

#ex rota
api.add_resource(Usuario, '/usuario/<int:id>')


if __name__ == '__main__':
    db.init_app(app)
    app.run(debug=True)