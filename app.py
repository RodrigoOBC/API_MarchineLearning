from flask import Flask
from textblob import TextBlob
import pandas as pd
from modelos.PrecoCasas import modelo

app = Flask('meu_APP')
model = modelo().linear_casa()

@app.route('/')
def home():
    return "Hello World!"


@app.route('/sentimento/<frase>')
def sentimento(frase):
    tb = TextBlob(frase)
    tb_en = tb.translate(to='en')
    polaridade = tb_en.sentiment.polarity
    return f"polaridade: {polaridade}"

@app.route('/prevercasa/<int:quartos>')
def cotacao(quartos):
    preco = model.predict([[quartos]])
    return f"preco: {preco}"


app.run(debug=True)
