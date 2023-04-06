from flask.views import MethodView
from flask import request, render_template, redirect
from src.db import mysql


class TestConstroller(MethodView):

    def get(self):
        with mysql.cursor() as cur:
            cur.execute('SELECT * FROM tb_produtos')
            dados = cur.fetchall()
            
        return render_template('public/index.html', data=dados)


    def post(self):
        id = request.form['id']
        codigo = request.form['codigo']
        nome = request.form['nome']
        qtd_est = request.form['qtd_est']
        preco = request.form['preco']
        fk_categoria = request.form['fk_categoria']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO tb_produtos VALUES(%s,%s,%s,%s,%s,%s)", (id, codigo,nome,qtd_est,preco,fk_categoria))
            cur.connection.commit()
            return redirect('/')
            
        # return 'Produto cadastrado com sucesso!'