from flask import Flask, jsonify, render_template, request, redirect, send_file, url_for
# import pandas as pd
from io import BytesIO
from Entidades.Veiculo import Veiculo
from Entidades.Cliente import Cliente
from Controle.ControleEstac import ControleEstac
from Controle.ControleVagas import ControleVaga
from Controle.ControleCliente import ControleCliente
from Controle.ControleVeiculo import ControleVeiculo
from Controle.ControlePlanos import ControlePlanos
from Controle.ControleHist import ControleHist
from Controle.ControlePagamento import ControlePagamento

app = Flask(__name__)
controleVaga = ControleVaga()
controleEstac = ControleEstac()
controleVaga = ControleVaga()
controleCliente = ControleCliente()
controleVeiculo = ControleVeiculo()
controlePlanos = ControlePlanos()
controleHist = ControleHist()
controlePag = ControlePagamento()

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
# Fim Index

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
    
    controleEstac.addVeiculoAvulso(veiculo)
    controleVaga.mudaEstadoVaga(vaga)
    controleHist.addHistorico(veiculo, vaga)
    return redirect("/registarveiculo")

@app.route("/buscarveiculo")
def buscarVeiculo():
    placa = request.args.get("placa")
    dados = controleEstac.buscarVeiculoAvulso(placa)
    if dados:
        return jsonify({**dados, "encontrado": True})
    else:
        return jsonify({"encontrado": False})
# Fim do registrar veiculo
  
# pagamento avulsos envio
@app.route("/pagamentoavulso", methods=["POST"])
def pagamentoAvulso():
    dados = request.get_json()
    print("Dados recebidos:", dados)

    modelo = dados['modeloCarro'] if 'modeloCarro' in dados else None
    cor = dados['corCarro'] if 'corCarro' in dados else None
    placa = dados['placaCarro'] if 'placaCarro' in dados else None
    vaga = dados['vaga'] if 'vaga' in dados else None

    veiculo = Veiculo(placa, modelo, cor)
    controlePag.realizarPagamentoAvulso(placa)
    controleEstac.trocaEstadoVeiculo(veiculo)
    controleVaga.mudaEstadoVaga(vaga)

    return jsonify({
        "redirect": url_for('indexPagamentosAvulsos', placa=placa, modelo=modelo, cor=cor)
    })
   
# Fim pagamento avulsos envio

# pagina pagamentos
@app.route("/indexpagamentosavulsos")
def indexPagamentosAvulsos():
    placa = request.args.get("placa")
    modelo = request.args.get("modelo")
    cor = request.args.get("cor")

    veiculo = Veiculo(placa, modelo, cor)
    dados = controlePag.getPagamentoAvulso(veiculo)
    print("dados do pagamento:", dados)

    return render_template("pagamento.html", dados=dados)
# Fim pagina pagamentos
    
@app.route("/feedback")
def paginaFeedback():
    return render_template("feedback.html")

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
    controleVaga.mudaEstadoVaga(vaga)
    
    
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
    controleEstac.trocaEstadoVeiculo(veiculo)

    return redirect("/cadastrarcliente")

@app.route("/registrarsaidacliente", methods = ["POST"])
def registrarSaidaCliente():
    modelo = request.form.get('modeloCliente')
    cor = request.form.get('corCliente')
    placa = request.form.get('placaCliente')

    veiculo = Veiculo(placa, modelo, cor)
    controleHist.addInfoSaida(veiculo)
    controleEstac.trocaEstadoVeiculo(veiculo)

    return redirect("/cadastrarcliente")
#Fim cadastro do cliente    

    #Rota para o relatorio do Financeirooo mensal
# @app.route("/download/relatorio")
# def download_relatorio():
#     tipo = request.args.get("tipo", default="mensal")  # pega tipo da query string

#     try:
#         conexao = ConexaoBD()
        
#         if tipo == "diario":
#             query = "SELECT * FROM vw_pgto_diario"
#             nome_arquivo = "relatorio_diario.xlsx"
#         else:  # padrão é mensal
#             query = "SELECT * FROM vw_pgto_mensal"
#             nome_arquivo = "relatorio_mensal.xlsx"

#         conexao.cursor.execute(query)
#         colunas = [desc[0] for desc in conexao.cursor.description]
#         dados = conexao.cursor.fetchall()
#         conexao.fecharConexao()

#         df = pd.DataFrame(dados, columns=colunas)

#         output = BytesIO()
#         with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
#             df.to_excel(writer, index=False, sheet_name='Relatório')
#         output.seek(0)

#         return send_file(
#             output,
#             download_name=nome_arquivo,
#             as_attachment=True,
#             mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
#         )
#     except Exception as e:
#         return f"Erro ao gerar relatório: {e}", 500



if __name__ == "__main__":
    app.run(debug=True)
