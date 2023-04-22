from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Esse é o trabalho final do Grupo 28 V2"

if __name__ == '__main__':
    app.run()
