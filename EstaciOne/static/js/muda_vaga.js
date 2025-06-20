window.onload = function () {
    ocuparVagas();
}

function ocuparVagas() {
    fetch(`/verificarvagas`)
        .then(response => response.json())
        .then(vagas => {
            // Primeiro: marca todas como livres
            document.querySelectorAll(".vaga").forEach(div => {
                const img = div.querySelector("img");
                const imagemVazia = div.getAttribute("data-imagem-vazia");
                div.setAttribute("data-ocupada", "false");
                img.src = imagemVazia;
            });

            // Agora: marca como ocupadas as que o backend mandou
            vagas.forEach(vaga => {
                const divVaga = document.getElementById(vaga.localizacao);
                if (divVaga) {
                    const img = divVaga.querySelector("img");
                    const imagemOcupada = divVaga.getAttribute("data-imagem-ocupada");
                    divVaga.setAttribute("data-ocupada", "true");
                    img.src = imagemOcupada;
                }
            });
        });
}
