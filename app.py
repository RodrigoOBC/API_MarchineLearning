from flask import Flask
from textblob import TextBlob

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


app.run(debug=True)
