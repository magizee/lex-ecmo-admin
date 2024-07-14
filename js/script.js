document.getElementById('controlButton').addEventListener('click', sendCommand);

function sendCommand() {
    fetch('/command', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ action: 'some_action' })
    })
    .then(response => response.json())
    .then(data => {
        if (data.status === 'success') {
            alert('Command sent successfully!');
        } else {
            alert('Failed to send command.');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error sending command.');
    });
}
