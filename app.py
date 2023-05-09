from flask import Flask, request, render_template
from flask_mysqldb import MySQL

app = Flask("__name__")

app.config['MYSQL_HOST'] = '127.0.0.1'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fatec'
app.config['MYSQL_DB'] = 'faculdade'

mysql = MySQL(app)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/home")
def home2():
    return render_template("home.html")

@app.route("/quemsomos")
def quemsomos():
    return render_template("quemsomos.html")

@app.route("/contato", methods=['GET', 'POST'])
def contato():
    if request.method == "POST":
        email = request.form['email']
        assunto = request.form['assunto']
        descricao = request.form['descricao']

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO contato(email, assunto, descricao) VALUES (%s, %s, %s)", (email, assunto, descricao))

        mysql.connection.commit()

        cur.close()

        return 'Informações enviadas ao banco de dados :)'
    return render_template("contato.html")

