##definindo uma pagina;
from app import app 


@app.route("/index")
@app.route("/")
def index():
    return "Hello World"

@app.route("/test" , defaults ={'name':None})
@app.route("/test/<name>")
def test(name):
	if(name):
		return "O %s ta aprendendo rotas" %name
	else:
		return "Alguém está aprendendo rotas"