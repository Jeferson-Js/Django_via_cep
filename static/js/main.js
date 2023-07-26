const form = document.getElementById('cep-form');
    const resultDiv = document.getElementById('result');

    form.addEventListener('submit', (e) => {
        e.preventDefault();
        const formData = new FormData(form);
        fetch(`/get_cep/?${new URLSearchParams(formData).toString()}`)
            .then(response => response.json())
            .then(data => {
                if (data.erro) {
                    resultDiv.innerHTML = 'CEP não encontrado';
                } else {
                    const enderecoCompleto = data.logradouro + ', ' + (formData.get('numero') || 'S/N');
                    resultDiv.innerHTML = `
                        <p>CEP: ${data.cep}</p>
                        <p>Endereço: ${enderecoCompleto}</p>
                        <p>Bairro: ${data.bairro}</p>
                        <p>Cidade/UF: ${data.localidade}/${data.uf}</p>
                    `;
                }
                // Limpar o campo de CEP e número após o envio.
                form.reset();
            })
            .catch(error => console.error('Erro na requisição:', error));
    });