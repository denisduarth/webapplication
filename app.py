# Ao abrir o gitpod, execute:
# pip install -r requirements.txt

from flask import Flask, render_template, request, redirect
from uuid import uuid4
import csv

app = Flask(__name__)

lista_livros = [
    {'id': uuid4(), 'autor': 'Machado de Assis', 'título': 'Memórias Póstumas de Brás Cubas', 'situação': 'Lido'},
    {'id': uuid4(), 'autor': 'Stephen King', 'título': 'It, a Coisa', 'situação': 'Não lido'},
    {'id': uuid4(), 'autor': 'Edgar Allan Poe', 'título': 'O corvo', 'situação': 'Não lido'},
]

@app.route('/')
def index():
    with open('lista_de_livros.csv', 'wt') as file_out:
        escritor = csv.DictWriter(file_out, ['id', 'autor', 'título', 'situação'])
        escritor.writeheader()
        escritor.writerows(lista_livros)
        file_out.close()
 
    with open('lista_de_livros.csv','rt') as file_in:
        leitura = csv.DictReader(file_in)
        csv.reader(file_in)
        file_in.close()
    
    return render_template('index.html',lista_livros = lista_livros)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/save', methods=['POST'])
def save():
    autor = request.form['Autor'].capitalize()
    titulo = request.form['Título'].capitalize()
    situacao = request.form['Situação'].capitalize()
    lista_livros.append({'id':uuid4(),'autor': autor,'título': titulo,'situação': situacao})
    return redirect("/")

@app.route('/delete/<id>')
def delete(id):
    for livro in lista_livros:
        if id == str(livro['id']):
            lista_livros.remove(livro)
            return redirect("/")

@app.route('/edit/<id>')
def edit(id):
    for livro in lista_livros:
        if id == str(livro['id']):
            livro == livro['id']
        return render_template('update.html')

@app.route('/update/<id>')
def update(id):
    try:
        novo_autor = request.form['Autor'].capitalize()
        novo_titulo = request.form['Título'].capitalize()
        nova_situacao = request.form['Situação'].capitalize()
        
        for livro in lista_livros:
            if id == str(livro['id']):
                livro['autor'] = novo_autor
                livro['título'] = novo_titulo
                livro['situação'] = nova_situação
                lista_livros[lista_livros.index(livro)] = ({'id':id,'autor':novo_autor,'título':novo_titulo,'situação':nova_situacao})
                
                with open('lista_de_livros.csv', 'wt') as file_out:
                    escritor = csv.DictWriter(file_out, ['id', 'autor', 'título', 'situação'])
                    escritor.writeheader()
                    escritor.writerows(livro)
                    file_out.close()
                
                return redirect("/")
    
    except:
        return 'Aconteceu algo de errado'

app.run(debug=True)