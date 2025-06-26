function buscarCliente(){
    const cpf = document.getElementById("pesquisaCliente").value;

    fetch(`/buscarcliente?cpf=${encodeURIComponent(cpf)}`)
    .then(response => response.json())
    .then(data => {
            document.getElementById("nomeCliente").value = data.nome;
            document.getElementById("cpfCliente").value = data.cpf;
            document.getElementById("foneCliente").value = data.telefone;
            document.getElementById("emailCliente").value = data.email;

            document.querySelectorAll("select[name = 'plano']").forEach(select =>{
                let option = Array.from(select.options).find(opt => opt.value === data.plano);
                if (!option) {
                    // Cria e adiciona a opção se não existir
                    option = new Option(data.plano, data.plano);
                    select.add(option);
                }

                select.value = data.plano;
            });
            document.querySelectorAll("select[name = 'vaga']").forEach(select =>{
                let option = Array.from(select.options).find(opt => opt.value === data.vaga);
                if (!option) {
                    // Cria e adiciona a opção se não existir
                    option = new Option(data.vaga, data.vaga);
                    select.add(option);
                }

                select.value = data.vaga;
            });

            document.getElementById("modeloCliente").value = data.modelo;
            document.getElementById("corCliente").value = data.cor;
            document.getElementById("placaCliente").value = data.placa;
    });
}

function enviarPara(rota) {
    const form = document.getElementById('formCliente');
    form.action = rota;
    form.submit();
}
