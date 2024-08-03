function updateSliders() {
    fetch()
        .then(response => response.json());
    console.log(response.json());
    console.log('HI');
}


setInterval(updateSliders, 20);