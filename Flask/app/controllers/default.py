##definindo uma pagina;
from app import app,db
from flask import render_template, request
from app.models.forms import LoginForm
from app.models.tables import User


@app.route("/index/")
@app.route("/")
def index():
    return render_template('index.html')


@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', form = form)



@app.route("/teste",methods = ['POST'])
def teste():
	valor = request.get_json(silent=True)
	user = User(valor['Username'], valor['Email'], valor['Password'], valor['Name'])
	db.session.add(user)
	db.session.flush()
	db.session.commit()
	print(user.id)
	return 'O cadastro falhou.'