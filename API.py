import webbrowser
from flask import Flask

webbrowser.open("http://localhost:5000")

app = Flask(__name__)

@app.route('/')
def index():
    with open("tarefas.txt", "r") as arquivo:
        conteudo = arquivo.read()
    return conteudo

if __name__ == '__main__':
    app.run(debug=True)
