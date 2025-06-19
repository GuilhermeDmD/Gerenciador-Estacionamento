function buscarVeiculo(){
    const placa = document.getElementById("pesquisaPlaca").value;

    // recebe os parâmetros do veículo por JSON
    fetch(`/buscarveiculo?placa=${encodeURIComponent(placa)}`)
    .then(response => response.json())
    .then(data => {
        // if(data.encontrado = false){
            document.getElementById("modeloCarro").value = data.modelo;
            document.getElementById("corCarro").value = data.cor;
            document.getElementById("placaCarro").value = data.placa;
            const select = document.getElementById("vaga");
            let option = Array.from(select.options).find(opt => opt.value === data.vaga);
            if (!option) {
                // Cria e adiciona a opção se não existir
                option = new Option(data.vaga, data.vaga);
                select.add(option);
            }

            select.value = data.vaga;
        // }else{
        //     alert("Dados não encontrados");
        // }
    });
}