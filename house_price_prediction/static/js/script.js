document.getElementById('prediction-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const location = document.getElementById('location').value;
    const size = parseFloat(document.getElementById('size').value);
    const bedrooms = parseInt(document.getElementById('bedrooms').value);
    const bathrooms = parseInt(document.getElementById('bathrooms').value);

    // Create data object to send to API
    const data = { location, size, bedrooms, bathrooms };

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(result => {
        const price = result.price;
        document.getElementById('price').textContent = `± Rp. ${price.toLocaleString()}`;
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
