function enviarParaPagamento() {
    const modelo = document.getElementById("modeloCarro").value;
    const cor = document.getElementById("corCarro").value;
    const placa = document.getElementById("placaCarro").value;
    const vaga = document.getElementById("vaga").value

    fetch("/pagamentoavulso", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            modeloCarro: modelo,
            corCarro: cor,
            placaCarro: placa,
            vaga: vaga
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;  // Redireciona para a página de pagamento
        }
    })
    .catch(error => {
        console.error("Erro ao enviar dados para pagamento:", error);
    });
}
