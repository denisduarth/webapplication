# Ao abrir o gitpod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request
from uuid import uuid4

app = Flask(__name__)

lista_livros = [
    {'id': uuid4(), 'autor': 'machado de assis', 'título': 'memórias póstumas de brás cubas', 'situação': 'lido'},
    {'id': uuid4(), 'autor': 'stephen king', 'título': 'it, a coisa', 'situação': 'não lido'},
    {'id': uuid4(), 'autor': 'edgar allan poe', 'título': 'o corvo', 'situação': 'não lido'},
]

@app.route('/')
def index():
    return render_template('index.html',lista_livros = lista_livros)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/save', methods=['POST'])
def save():
    autor = request.form['Autor']
    titulo = request.form['Título']
    situação = request.form['Situação']
    lista_livros.append({'id': uuid4(),'autor': autor,'título': titulo,'situação': situação})
    return render_template('index.html', lista_livros=lista_livros)

@app.route('/update/<id>', methods=['POST'])
def edit():
    return add()

@app.route('/delete/<id>')
def delete():
    del lista_livros['id']





app.run(debug=True)