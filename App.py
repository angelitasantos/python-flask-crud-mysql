from flask import Flask, render_template, request, redirect, url_for
from database import *


app = Flask(__name__)

app.secret_key = 'flash message'

self = 'self'
conexao = MySQL.conexao(self)

@app.errorhandler(404)
def not_found(e):
    title = 'Error 404'
    return render_template('/pages/error404.html', title=title)

@app.route('/')
def home():
    title = 'Home'
    return render_template('/pages/home.html', title=title)

@app.route('/about')
def about():
    title = 'About'
    return render_template('/pages/about.html', title=title)

@app.route('/contact')
def contact():
    title = 'Contact'
    return render_template('/pages/contact.html', title=title)

@app.route('/crud')
def crud():
    title = 'CRUD'
    self = 'self'
    data = MySQL.read(self)
    return render_template('crud.html', title=title, students = data)

@app.route('/create', methods = ['POST'])
def create():
    self = 'self'
    MySQL.create(self)
    return redirect(url_for('crud'))

if __name__ == '__main__':
    app.run(debug = True)