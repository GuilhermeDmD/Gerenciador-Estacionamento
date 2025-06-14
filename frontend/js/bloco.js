document.addEventListener('DOMContentLoaded', function() {
    const notepad = document.getElementById('notepad');
    const localStorageKey = 'myNotepadContent'; // Chave para armazenar no localStorage

    const savedContent = localStorage.getItem(localStorageKey);
    if (savedContent) {
        notepad.value = savedContent; 
    }

    notepad.addEventListener('input', function() {

        localStorage.setItem(localStorageKey, notepad.value); 
    });

    if (typeof(Storage) === "undefined") {
        alert('Seu navegador não suporta salvamento automático. Por favor, atualize-o!');
        notepad.disabled = true; 
    }
});