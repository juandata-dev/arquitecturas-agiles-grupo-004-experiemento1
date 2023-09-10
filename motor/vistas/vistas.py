from flask import request, make_response
from flask_restful import Resource
from faker import Faker
import random
import json

class Candidato(dict):
    def __init__(self, name, email_address, title, phone_number=None):
        dict.__init__(self, 
                      name=name, 
                      email_address = email_address,
                      title = title,
                      phone_number = phone_number)


class VistaCandidatos(Resource):    
    def get(self):
        data_factory = Faker()
        candidatos_creados = []
        is_a_fail = random.randint(1, 100)

        if is_a_fail < 15:
            return 'Service Unavailable', 503
        else:

            for i in range(0,10):
                #Crear los datos del ingrediente
                name = data_factory.name()
                email_address = data_factory.ascii_email()
                title = data_factory.job()
                phone_number = data_factory.phone_number()
                
                #Crear el candidato con los datos aleatorios
                candidato = Candidato(name = name,
                                    email_address=email_address,
                                    title=title,
                                    phone_number=phone_number)
                candidatos_creados.append(candidato)
            
            data = [json.dumps(candidato) for candidato in candidatos_creados]
            resp = make_response(json.dumps(data), 200)
            resp.headers.extend({})
        
            return resp