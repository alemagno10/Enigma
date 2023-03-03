from __future__ import annotations
from model.sql_alchemy_para_db import db
from datetime import datetime
from flask_bcrypt import generate_password_hash, check_password_hash

class UsuarioModel(db.Model):
    __tablename__ = "usuario_model"

    id = db.Column(db.Integer, primary_key=True )
    nome = db.Column(db.String(80) , unique = True , nullable = False)
    senha = db.Column(db.String(60) , nullable = False)

    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    @classmethod
    def search_all(cls):
        return cls.query.all()    


