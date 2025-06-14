const menu = document.getElementById("menu-contexto");
let vagaCliclada = null;

// Mostrar o menu ao clicar com botão direito em qualquer vaga
document.querySelectorAll(".vaga").forEach(vaga => {
    vaga.addEventListener("contextmenu", function (e) {
        e.preventDefault();

        // Armazena a vaga que foi clicada
        vagaCliclada = vaga;

        // Posiciona o menu
        menu.style.display = "block";
        menu.style.left = `${e.pageX}px`;
        menu.style.top = `${e.pageY}px`;
    });
});

// Ocultar o menu ao clicar em qualquer outro lugar
document.addEventListener("click", function (e) {
    // Se clicar fora do menu, esconde
    if (!menu.contains(e.target)) {
        menu.style.display = "none";
    }
});

document.querySelectorAll("#menu-contexto li").forEach(item =>{
    item.addEventListener("click", function(){
        const acao = this.getAttribute("data-acao");

        if(!vagaCliclada) return;

        switch(acao){
            case "adicionarVeiculo":
                adicionarVeiculo(vagaCliclada);
                break;
            case "finalizarVeiculo":
                finalizarVeiculo(vagaCliclada);
                break;
            case "cancelar":
                cancelar(vagaCliclada);
        }
          menu.style.display = "none";
    })
})

function adicionarVeiculo(vaga){
    window.location.href = "RegistrarVeiculos.html";
    
}
function finalizarVeiculo(vaga){
    alert(vaga);
    
}
function cancelar(vaga){
    document.addEventListener("click", function (e) {
    // Se clicar fora do menu, esconde
    
        menu.style.display = "none";
});
}