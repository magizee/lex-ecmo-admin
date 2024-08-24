function fetchStatus() {
    fetch('/api/status')
        .then(response => response.json())
        .then(data => {
            document.getElementById('flow_rate').innerText = data.flow_rate;
            document.getElementById('p_ven').innerText = data.p_ven;
            document.getElementById('p_int').innerText = data.p_int;
            document.getElementById('p_art').innerText = data.p_art;
            document.getElementById('t_art').innerText = data.t_art;
            document.getElementById('svo2').innerText = data.svo2;
            document.getElementById('delta_p').innerText = data.delta_p;
            document.getElementById('rpm').innerText = data.rpm;
            
            // Update row classes based on safety status
            updateRowClass('flow_rate', data.safety_status.flow_rate);
            updateRowClass('p_ven', data.safety_status.p_ven);
            updateRowClass('p_int', data.safety_status.p_int);
            updateRowClass('p_art', data.safety_status.p_art);
            updateRowClass('t_art', data.safety_status.t_art);
            updateRowClass('svo2', data.safety_status.svo2);
            updateRowClass('delta_p', data.safety_status.delta_p);
        });
}

function updateRowClass(id, isSafe) {
    const row = document.getElementById(`${id}_row`);
    if (isSafe) {
        row.classList.add('safe');
        row.classList.remove('unsafe');
    } else {
        row.classList.add('unsafe');
        row.classList.remove('safe');
    }
}

// Fetch status every second
setInterval(fetchStatus, 1000);

// Initial fetch to populate data
window.onload = fetchStatus;
