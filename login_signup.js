// Sign-up form validation and submission
document.getElementById('signupForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Error message spans
    let firstNameError = document.getElementById('firstNameError');
    let lastNameError = document.getElementById('lastNameError');
    let emailError = document.getElementById('emailError');
    let passwordError = document.getElementById('passwordError');

    // Clear previous error messages
    firstNameError.textContent = '';
    lastNameError.textContent = '';
    emailError.textContent = '';
    passwordError.textContent = '';

    // Inputs
    let firstName = document.getElementById('firstName').value.trim();
    let lastName = document.getElementById('lastName').value.trim();
    let email = document.getElementById('email').value.trim();
    let password = document.getElementById('password').value.trim();

    let isValid = true;

    // First Name validation
    if (firstName === '') {
        firstNameError.textContent = 'First name is required';
        isValid = false;
    }

    // Last Name validation
    if (lastName === '') {
        lastNameError.textContent = 'Last name is required';
        isValid = false;
    }

    // Email validation
    if (!validateEmail(email)) {
        emailError.textContent = 'Please enter a valid email address (e.g., name@example.com)';
        isValid = false;
    }

    // Password validation
    if (password.length < 6) {
        passwordError.textContent = 'Password must be at least 6 characters long';
        isValid = false;
    }

    // If the form is valid, redirect to index.html
    if (isValid) {
        alert('Sign up successful!');
        window.location.href = "index.html";
    }
});

// Login form submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    
    // Redirect to index.html after successful login
    alert('Login successfulx!');
    window.location.href = "index.html";
});

// Email validation function
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}
// Handle login form submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission
    
    // Redirect to login.html
    window.location.href = "login.html";
});
