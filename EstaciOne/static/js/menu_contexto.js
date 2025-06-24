const menu = document.getElementById("menu-contexto");
let vagaCliclada = null;

// Mostrar o menu ao clicar com botão direito em qualquer vaga
document.querySelectorAll(".vaga").forEach(vaga => {
    vaga.addEventListener("contextmenu", function (e) {
        e.preventDefault();

        // Armazena o valor da vaga (ex: "A1", "M3")
        vagaCliclada = vaga.id;

        // Posiciona o menu
        menu.style.display = "block";
        menu.style.left = `${e.pageX}px`;
        menu.style.top = `${e.pageY}px`;
    });
});

// Ocultar o menu ao clicar em qualquer outro lugar
document.addEventListener("click", function (e) {
    if (!menu.contains(e.target)) {
        menu.style.display = "none";
    }
});

document.querySelectorAll("#menu-contexto li").forEach(item => {
    item.addEventListener("click", function () {
        const acao = this.getAttribute("data-acao");

        if (!vagaCliclada) return;

        switch (acao) {
            case "adicionarVeiculo":
                adicionarVeiculo(vagaCliclada);
                break;
            case "finalizarVeiculo":
                finalizarVeiculo(vagaCliclada);
                break;
            case "cancelar":
                cancelar();
                break;
        }

        menu.style.display = "none";
    });
});

function adicionarVeiculo(vaga) {
    // Redireciona para página passando a vaga como parâmetro
    if(vaga.startsWith("A")){
        const url = `/registarveiculo?&vaga=${vaga}&contexto=registro`;
        window.location.href = url;
    }else if(vaga.startsWith("M")){
        // aqui redicionaria com os dados para a tela de entrada e saída do cliente
        window.location.href = `/`;
    }
    
}

function finalizarVeiculo(vaga) {
    if (vaga.startsWith("A")) {
        fetch(`/gerarpagamentopopup?vaga=${encodeURIComponent(vaga)}`)
        .then(response => response.json())
        .then(data => {
            const modelo = data.modelo;
            const cor = data.cor;
            const placa = data.placa;
            const vaga = data.vaga;

        const url = `/registarveiculo?modelo=${encodeURIComponent(modelo)}&cor=${encodeURIComponent(cor)}&placa=${encodeURIComponent(placa)}&vaga=${vaga}&contexto=pagamento`;
        window.location.href = url;
    });

    } else if (vaga.startsWith("M")) {
        // Aqui redicionaria para a tela de entrada e saída do cliente 
        window.location.href = `/buscarcliente`;
    } else {
        alert("Tipo de vaga desconhecido!");
    }
}

function cancelar() {
    menu.style.display = "none";
}
