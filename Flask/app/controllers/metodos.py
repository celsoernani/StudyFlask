from app import *
from app.models.tables import Partida, Time
from sqlalchemy import update

def refreshComponents(json):

    if( contains(1, json) ):
        return "Partida já existente!"
    else:
         newPartida = Partida(
            estadio = json['estadio'],
            data = json['data'],
            gols_casa = json['gols_casa'],
            gols_visitante    = json['gols_visitante'],
            id_visitante    = json['id_visitante'],
            id_casa    = json['id_casa'],
                          )

    db.session.add(newPartida)
    db.session.commit() 
    return "Partida cadastrada!"