document.getElementById('myForm').addEventListener('submit', function(event) {
    var input = document.getElementById('img');
    var files = input.files;
    
    if (files.length < 1) {
        alert('Por favor, selecciona al menos una foto.');
        event.preventDefault();
    } else if (files.length > 4) {
        alert('Solo se permiten un máximo de 4 fotos.');
        event.preventDefault();
    }
});