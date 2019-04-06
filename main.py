#Nome: Geraldo Pereira de Castro Junior
#RA: 21802596

from flask import Flask, request, render_template
from flaskext.mysql import MySQL
from bd import *

app = Flask(__name__)
mysql = MySQL()
mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'faculdade'

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/listarProfessores')
def listarprofessores():
    cursor = mysql.get_db().cursor()
    return render_template('listarprofessores.html', professores = get_professores(cursor))

@app.route('/professores/<professor>')
def detalhes_professor(professor):
    cursor = mysql.get_db().cursor()
    prof_details = get_prof_details(cursor, professor)
    cursor = mysql.get_db().cursor()
    prof_disciplinas = get_prof_disciplinas(cursor, professor)
    return render_template('detalhes.html',prof_details=prof_details, prof_disciplinas=prof_disciplinas)

@app.route('/consultarPorTitulacao')
def consulta_titulacao():
    titulacao = request.args.get('professortitulacao')
    print(titulacao)
    cursor = mysql.get_db().cursor()
    return render_template('listarprofessores.html', professores= get_form_titulacao(cursor,titulacao))

if __name__ == '__main__':
    app.run(debug=True)