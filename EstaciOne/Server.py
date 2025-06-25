from flask import Flask, jsonify, render_template, request, redirect
from Entidades.Veiculo import Veiculo
from Entidades.Cliente import Cliente
from Controle.ControleEstac import ControleEstac
from Controle.ControleVagas import ControleVaga
from Controle.ControleCliente import ControleCliente
from Controle.ControleVeiculo import ControleVeiculo
from Controle.ControlePlanos import ControlePlanos
from Controle.ControleHist import ControleHist

app = Flask(__name__)
controleVaga = ControleVaga()
controleEstac = ControleEstac()
controleVaga = ControleVaga()
controleCliente = ControleCliente()
controleVeiculo = ControleVeiculo()
controlePlanos = ControlePlanos()
controleHist = ControleHist()

# Index
@app.route("/")
def paginaInicial():
    return render_template("index.html")

@app.route("/verificarvagas")
def verificarVagas():
    dados = controleVaga.mostrarVagasOcupadas()
    print("Vagas ocupadas: ", dados)
    return jsonify(dados)

@app.route("/gerarpagamentopopup")
def gerarPagamentoPopUp():
    vaga = request.args.get("vaga")
    print("Vaga clicada: ", vaga)
    dados = controleEstac.buscarVeiculoAvulsoPorVaga(vaga)
    return jsonify(dados)

# registrar veiculo
@app.route("/registarveiculo")
def paginaRegistrarVeiculos():
    vagas = controleVaga.mostrarVagasAvulsas()
    return render_template("RegistrarVeiculos.html", vagas = vagas)

@app.route("/sendVeiculo", methods=['POST'])
def paginaRegistrar():
    modelo = request.form.get('modeloCarro')
    cor = request.form.get('corCarro')
    placa = request.form.get('placaCarro')
    vaga = request.form.get('vaga')
    veiculo = Veiculo(placa, modelo, cor)
    
#    adicionando os dados no banco de dados
    controleEstac.addVeiculoAvulso(veiculo)
    controleVaga.ocuparVaga(vaga)
    controleHist.addHistorico(veiculo, vaga)
    
    #precisa add no histórico tbm
    return redirect("/registarveiculo")

@app.route("/buscarveiculo")
def buscarVeiculo():
    placa = request.args.get("placa")
    dados = controleEstac.buscarVeiculoAvulso(placa)
    if dados:
        return jsonify({**dados, "encontrado": True})
    else:
        return jsonify({"encontrado": False})
    

# uma do finalizar
    
#tá pronto já
@app.route("/feedback")
def paginaFeedback():
    return render_template("feedback.html")

# histórico
@app.route("/historico")
def paginaHistorico():
    return render_template("Historico.html")

@app.route("/financeiro")
def paginaFinanceiro():
    return render_template("financeiro.html")

@app.route("/buscarhistorico")
def buscarHistorico():
    placa = request.args.get("placa")
    print("Placa achada:", placa)
    dados = controleHist.getHistorico(placa)
    print("Dados do histórico: ",dados)
    return jsonify(dados)


# tá pronto já
@app.route("/anotacoes")
def paginaAnotacoes():
    return render_template("Anotacoes.html")

# cadastro do cliente
@app.route("/cadastrarcliente")
def paginaCadastrarCliente():
    planos = controlePlanos.mostrarPlanos()
    vagas = controleVaga.mostrarVagasMensais()
    return render_template("cadastroCliente.html", vagas=vagas, planos=planos)

@app.route("/sendCliente", methods = ["POST"])
def cadastrarCliente():
    nome = request.form.get('nomeCliente')
    cpf = request.form.get('cpfCliente')
    telefone = request.form.get('foneCliente')
    email = request.form.get('emailCliente')
    plano = request.form.get('plano')
    vaga = request.form.get('vaga')

    modelo = request.form.get('modeloCliente')
    cor = request.form.get('corCliente')
    placa = request.form.get('placaCliente')

    novoCliente = Cliente(cpf, nome, telefone, email)
    novoVeiculo = Veiculo(placa, modelo, cor)

    controleCliente.addCliente(novoCliente, vaga, plano)
    controleVeiculo.addVeiculo(novoVeiculo, cpf)
    controleVaga.ocuparVaga(vaga)
    
    
    return redirect("/cadastrarcliente")

@app.route("/buscarcliente")
def buscarCliente():
    cpf = request.args.get("cpf")
    dados = controleCliente.buscarCliente(cpf)
    print("Dados do cliente pesquisado: ", dados)
    if dados:
        return jsonify({**dados, "encontrado": True})
    else:
        return jsonify({"encontrado": False})
    
@app.route("/registrarentradacliente", methods = ["POST"])
def registrarEntradaCliente():
    modelo = request.form.get('modeloCliente')
    cor = request.form.get('corCliente')
    placa = request.form.get('placaCliente')
    vaga = request.form.get('vaga')

    veiculo = Veiculo(placa, modelo, cor)
    controleHist.addHistorico(veiculo, vaga)
    controleEstac.trocaEstadoMensal(veiculo)

    return redirect("/cadastrarcliente")

@app.route("/registrarsaidacliente", methods = ["POST"])
def registrarSaidaCliente():
    modelo = request.form.get('modeloCliente')
    cor = request.form.get('corCliente')
    placa = request.form.get('placaCliente')

    veiculo = Veiculo(placa, modelo, cor)
    controleHist.addInfoSaida(veiculo)
    controleEstac.trocaEstadoMensal(veiculo)

    return redirect("/cadastrarcliente")


if __name__ == "__main__":
    app.run(debug=True)