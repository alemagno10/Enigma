from flask_restful import Resource
from flask import request, jsonify, render_template, redirect, url_for, make_response
from model.modelos import *
import os
import json

alfabeto_cifrado = "bcdefghijkl mnopqrstuvwxyza"
cifrador_auxiliar = "ijkl mnopqrstuvwxyzabcdefgh"

class Para_String(Resource):
    def post(self):
        corpo = request.get_json( force=True )
        string_crypt = para_string(np.array(corpo['chave']))
        return {'Chave em String': string_crypt}, 200
    
class Para_OneHot(Resource):
    def post(self):
        corpo = request.get_json( force=True )
        one_hot = para_one_hot(corpo['chave'])
        return {'Chave em One Hot': one_hot.tolist()}, 200

class Cifra(Resource):
    #cifra
    def post(self):
        corpo = request.get_json( force=True )
        string_crypt = cifra(corpo['mensagem'],para_one_hot(alfabeto_cifrado))
        return {'Mensagem Criptografada': string_crypt}, 200
    
class De_Cifra(Resource):
    #de cifra
    def post(self):
        corpo = request.get_json( force=True )
        string_crypt = de_cifra(corpo['mensagem'],para_one_hot(alfabeto_cifrado))
        return {'Mensagem Descriptografada': string_crypt}, 200
    
class Enigma(Resource):
    #enigma
    def post(self):
        corpo = request.get_json( force=True )
        string_crypt = enigma(corpo['mensagem'],para_one_hot(alfabeto_cifrado),para_one_hot(cifrador_auxiliar))
        return {'Mensagem Criptografada': string_crypt}, 200
    
class De_Enigma(Resource):
    #de enigma
    def post(self):
        corpo = request.get_json( force=True )
        string_crypt = de_enigma(corpo['mensagem'],para_one_hot(alfabeto_cifrado),para_one_hot(cifrador_auxiliar))
        return {'Mensagem Descriptografada': string_crypt}, 200

