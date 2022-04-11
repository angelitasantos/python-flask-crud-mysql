import mysql.connector
from flask import request, flash


self = 'self'
class MySQL:

    def __init__(self, conexao):
        self.conexao = conexao


    def conexao(self):
        conexao = mysql.connector.connect(
                host='localhost', 
                database='crudapplication', 
                user='root', 
                password='*********')
        return conexao


    def create(self):

        conexao = MySQL.conexao(self)

        if request.method == 'POST':

            flash("Data Created Successfully.")

            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']

            cursor = conexao.cursor()
            cursor.execute("INSERT INTO students(name, email, phone) VALUES(%s, %s, %s)", (name, email, phone))
            conexao.commit()

    
    def read(self):

        conexao = MySQL.conexao(self)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        cursor.close()
        return data

    
    
