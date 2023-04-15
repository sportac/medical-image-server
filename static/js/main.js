const form = document.querySelector('form');

// Login
form.addEventListener('submit', async (event) => {
    event.preventDefault();

    const formData = new FormData(form);

    const response = await fetch('/login', {
        method: 'POST',
        body: formData
    });

    if (response.ok) {
        window.location.href = '/home';
    } else if (response.status === 401) {
        alert('Invalid credentials');
    } else {
        alert('An error occurred');
    }

});

// Logout
const logoutButton = document.getElementById('logout-button');
logoutButton.addEventListener('click', () => {
  fetch('/logout', { method: 'GET' })
    .then(response => {
      if (response.ok) {
        // Redirect to login page after logout
        window.location.href = '/';
      } else {
        console.error('Failed to logout');
      }
    })
    .catch(error => console.error(error));
});
