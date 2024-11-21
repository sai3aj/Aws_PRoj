document.getElementById('appointment-form').addEventListener('submit', async function (event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const carModel = document.getElementById('car-model').value;
    const date = document.getElementById('date').value;

    const response = await fetch('/appointments', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ email, carModel, date }),
    });

    if (response.ok) {
        alert('Appointment booked successfully!');
    } else {
        alert('Failed to book appointment. Please try again.');
    }
});

document.getElementById('login-btn').addEventListener('click', function () {
    window.location.href = '/login';
});

document.getElementById('signup-btn').addEventListener('click', function () {
    window.location.href = '/signup';
});
