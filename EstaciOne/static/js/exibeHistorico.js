function buscarHistorico(){
    const placa = document.getElementById("placaHist").value;

     fetch(`/buscarhistorico?placa=${encodeURIComponent(placa)}`)
        .then(response => response.json())
        .then(data => {
            const resultado = document.getElementById("resultadoHistorico");
            resultado.innerHTML = data.historico;
        });
}