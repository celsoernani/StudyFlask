import os.path
from app import app,db
from flask import render_template, request
from app.models.tables import Time, Partida
from sqlalchemy import text
from sqlalchemy import create_engine
from sqlalchemy.sql import select







@app.route("/teste",methods = ['POST'])	
def teste():
	valor = (request.json.get('id'))
	conn = db.engine.connect()
	sql = text('SELECT estadio, data, gols_casa, gols_visitante FROM patidas WHERE id=:valor')
	sql1 = text('SELECT t.nomeTime FROM patidas AS p INNER JOIN times AS t ON (t.id=p.id_visitante) WHERE p.id=:valor')
	sql2 = text('SELECT t.nomeTime FROM patidas AS p INNER JOIN times AS t ON (t.id=p.id_casa) WHERE p.id=:valor')
	result = conn.execute(sql,valor=valor).fetchall()
	result1 = conn.execute(sql1,valor=valor).fetchall()
	result2 = conn.execute(sql2,valor=valor).fetchall()

	print(result[0]['estadio'])
	print(result[0]['data'])
	print(result[0]['gols_casa'])
	print(result[0]['gols_visitante'])
	print(result1[0]['nomeTime'])
	print(result2[0]['nomeTime'])

	return "Refresh Complete"