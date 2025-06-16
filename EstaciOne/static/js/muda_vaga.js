document.querySelectorAll('.vaga').forEach(vaga => {
    vaga.addEventListener('click', () => {
        const ocupada = vaga.getAttribute('data-ocupada') === 'true';
        const img = vaga.querySelector('img');
        const imagemVazia = vaga.getAttribute('data-imagem-vazia');
        const imagemOcupada = vaga.getAttribute('data-imagem-ocupada');

        if (ocupada) {
            img.src = imagemVazia;
            vaga.setAttribute('data-ocupada', 'false');
        } else {
            img.src = imagemOcupada;
            vaga.setAttribute('data-ocupada', 'true');
        }
    });
});