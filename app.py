from flask import Flask

app = Flask('meu_APP')


@app.route('/')
def home():
    return "Hello World!"


app.run()
