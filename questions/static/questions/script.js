document.getElementById('imagem').addEventListener('change', function(event) {
    const file = event.target.files[0];
    const reader = new FileReader();

    reader.onload = function(e) {
        const imgId = 'img_' + new Date().getTime();

        const img = document.createElement('img');
        img.src = e.target.result;

        img.style.width = "150px"; // Define o tamanho fixo da imagem
        img.style.display = "block";
        img.style.margin = "10px 0";

        // Insere a imagem visualmente no enunciado
        const enunciado = document.getElementById('enunciado');
        enunciado.appendChild(img);

        // Adiciona a imagem ao campo oculto para envio ao backend
        const imgInput = document.createElement('input');
        imgInput.type = 'hidden';
        imgInput.name = 'imagens';
        imgInput.value = JSON.stringify({ id: imgId, data: e.target.result });
        document.getElementById('questaoForm').appendChild(imgInput);
    }

    if (file) {
        reader.readAsDataURL(file);
    }
});

document.getElementById('questaoForm').addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(this);
    formData.append('enunciado', document.getElementById('enunciado').innerHTML);

    fetch('/questions/salvar_questao/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            window.location.href = "/questions/lista_questoes/";
        } else {
            alert("Erro ao salvar a questão.");
        }
    })
    .catch(error => console.error('Erro:', error));
});
