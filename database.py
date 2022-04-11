import mysql.connector
from flask import request, flash


self = 'self'
class ConexaoMySQL:

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

        conexao = ConexaoMySQL.conexao(self)

        if request.method == 'POST':

            flash("Data Created Successfully.")

            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']

            cursor = conexao.cursor()
            cursor.execute("""
            INSERT INTO students(name, email, phone) 
            VALUES(%s, %s, %s)""", (name, email, phone))
            conexao.commit()

    
    def read(self):

        conexao = ConexaoMySQL.conexao(self)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM students")
        data = cursor.fetchall()
        cursor.close()
        return data

    
    def update(self):

        conexao = ConexaoMySQL.conexao(self)

        if request.method == 'POST':

            flash("Data Updated Successfully.")

            id_data = request.form['id']
            name = request.form['name']
            email = request.form['email']
            phone = request.form['phone']

            cursor = conexao.cursor()
            cursor.execute("""
            UPDATE students
            SET name = %s, email = %s, phone = %s
            WHERE id = %s
            """, (name, email, phone, id_data))
            conexao.commit()


    def delete(self, id_data):

        conexao = ConexaoMySQL.conexao(self)

        flash("Data Deleted Successfully.")

        cursor = conexao.cursor()
        sql = "DELETE FROM students WHERE id = %s"
        id = (id_data, )
        cursor.execute(sql, id)
        conexao.commit()
