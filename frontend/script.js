document.getElementById('dataForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    if (name && email) {
        // Logic to send data to backend (use fetch API)
    } else {
        alert('Please fill in all fields');
    }
});
