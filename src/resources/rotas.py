from flask_restful import Resource
from flask import request, jsonify, render_template, redirect, url_for, make_response
from model.modelos import UsuarioModel, DesafiosModel, TagModel, AcertoModel
from model.sql_alchemy_para_db import db
import os
from model.forms import LoginForm, CadastroForm
import json

# para acessar usuario logado que nem faziamos no django, usar current_user+

class Usuario(Resource):
    usuario = []
    def get(self, id):
        usuario = UsuarioModel.find_by_id(id)

        if usuario:
            return usuario.toDict()

        return {'id': None}, 404
    
    def delete(self, id):
        usuario = UsuarioModel.find_by_id(id)

        if usuario:
            desafios = DesafiosModel.query.filter_by(usuario_id=id).all()
            for d in desafios:
                d.delete()
            usuario.delete()
            return {'mensagem': 'Usuario deletado da base.'}, 201

        return {'mensagem': 'Usuario não encontrado.'}, 404
