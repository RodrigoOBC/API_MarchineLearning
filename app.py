from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob import TextBlob
import pandas as pd
from modelos.PrecoCasas import modelo

app = Flask('meu_APP')


@app.route('/')
def home():
    return "Hello World!"


@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity
    return f"polaridade: {polaridade}"


@app.route('/prevercasa/', methods=['POST'])
def cotacao():
    coluna = ['Ano', 'QtQuartos', 'QTbanheiros', 'GaragemArea']
    model = modelo(coluna).linear_casa()
    dados = request.get_json()
    coluna = ['Ano', 'QtQuartos', 'QTbanheiros', 'GaragemArea']
    dados_json = [dados[col] for col in coluna]
    preco = model.predict([dados_json])
    return jsonify(preco=preco[0])

app.run(debug=True)
