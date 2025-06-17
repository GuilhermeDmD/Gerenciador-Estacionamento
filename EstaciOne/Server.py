from flask import Flask, render_template, request, redirect
from Entidades.Veiculo import Veiculo
from Controle.ControleEstac import ControleEstac
from Controle.ControleVagas import ControleVaga

app = Flask(__name__)

@app.route("/")
def paginaInicial():
    return render_template("index.html")

@app.route("/registarveiculo")
def paginaRegistrarVeiculos():
    return render_template("RegistrarVeiculos.html")

@app.route("/send", methods=['POST'])
def paginaRegistrar():
    modelo = request.form.get('modeloCarro')
    cor = request.form.get('corCarro')
    placa = request.form.get('placaCarro')
    vaga = request.form.get('vagaCarro')
    veiculo = Veiculo(placa, modelo, cor)
    controleEstac = ControleEstac()
    controleVaga = ControleVaga()
    controleEstac.addVeiculoAvulso(veiculo)
    controleVaga.ocuparVaga(vaga)
    #precisa add no histórico tbm
    return redirect("/registarveiculo")

# uma do finalizar, outra do buscar
    
#tá pronto já
@app.route("/feedback")
def paginaFeedback():
    return render_template("feedback.html")

@app.route("/historico")
def paginaHistorico():
    return render_template("Historico.html")

# tá pronto já
@app.route("/anotacoes")
def paginaAnotacoes():
    return render_template("Anotacoes.html")

@app.route("/cadastrarcliente")
def paginaCadastrarCliente():
    return render_template("cadastroCliente.html")

if __name__ == "__main__":
    app.run()