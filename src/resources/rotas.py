from flask_restful import Resource
from flask import request, jsonify, render_template, redirect, url_for, make_response
from model.modelos import *
import os
import json

class Para_String(Resource): ##opiniao ale se ja faz auto
    def post(self):
        corpo = request.get_json( force=True )
        string_crypt = para_string(np.array(corpo['chave']))
        return {'Chave em String': string_crypt}, 200
    
class Para_OneHot(Resource): ##esse funfou
    def post(self):
        corpo = request.get_json( force=True )
        one_hot = para_one_hot(corpo['chave'])
        return {'Chave em One Hot': one_hot.tolist()}, 200

class Cifra(Resource):
    #cifra
    def post(self):
        corpo = request.get_json( force=True )
        string_crypt = cifra(corpo['mensagem'],corpo['chave'])
        return {'Mensagem Criptografada': string_crypt}, 200
    
class De_Cifra(Resource):
    #de cifra
    def post(self):
        #verificação msg e M falta aqui
        corpo = request.get_json( force=True )
        string_crypt = de_cifra(corpo['mensagem'],corpo['chave'])
        return {'Mensagem Descriptografada': string_crypt}, 200
    
class Enigma(Resource):
    #enigma
    def post(self):
        #verificação msg, P e E falta aqui
        corpo = request.get_json( force=True )
        string_crypt = enigma(corpo['mensagem'],corpo['chave'],corpo['chave auxiliar'])
        return {'Mensagem Criptografada': string_crypt}, 200
    
class De_Enigma(Resource):
    #de enigma
    def post(self):
        #verificação msg, P e E falta aqui
        corpo = request.get_json( force=True )
        string_crypt = de_enigma(corpo['mensagem'],corpo['chave'],corpo['chave auxiliar'])
        return {'Mensagem Descriptografada': string_crypt}, 200

