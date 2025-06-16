from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def paginaInicial():
    return render_template("index.html")

@app.route("/registarveiculo")
def paginaRegistrarVeiculos():
    return render_template("RegistrarVeiculos.html")

@app.route("/feedback")
def paginaFeedback():
    return render_template("feedback.html")

@app.route("/historico")
def paginaHistorico():
    return render_template("Historico.html")

@app.route("/anotacoes")
def paginaAnotacoes():
    return render_template("Anotacoes.html")

@app.route("/cadastrarcliente")
def paginaCadastrarCliente():
    return render_template("cadastroCliente.html")

if __name__ == "__main__":
    app.run()