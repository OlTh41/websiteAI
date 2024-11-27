document.addEventListener('DOMContentLoaded', () => {
    const loginForm = document.getElementById('loginForm');
    const loginLink = document.getElementById('loginLink');
    const navbar = document.querySelector('nav ul');

    if (loginForm) {
        loginForm.addEventListener('submit', (e) => {
            e.preventDefault();
            const username = document.getElementById('username').value;
            const password = document.getElementById('password').value;

            if (username === 'test' && password === 'test') {
                localStorage.setItem('loggedIn', 'true');
                window.location.href = 'index.html';
            }
             else {
                alert('Invalid username or password');
            }
        });
    }


    const loggedIn = localStorage.getItem('loggedIn') === 'true';
    if (loggedIn) {
        loginLink.textContent = 'Logout';
        loginLink.href = '#';
        loginLink.addEventListener('click', (e) => {
            e.preventDefault();
            localStorage.removeItem('loggedIn');
            window.location.reload();
        });


        const newMenuItem = document.createElement('li');
        const newLink = document.createElement('a');
        newLink.href = 'Admin.html';
        newLink.textContent = 'Admin panel';
        newMenuItem.appendChild(newLink);
        navbar.appendChild(newMenuItem);
    }

    const copytext = "© 2024 Slimmeprullenbak. All rights reserved.";
    document.getElementById("copyright").textContent = copytext;
});