// Login form validation and submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();

    // Error message spans
    let emailError = document.getElementById('emailError');
    let passwordError = document.getElementById('passwordError');

    // Clear previous error messages
    emailError.textContent = '';
    passwordError.textContent = '';

    // Inputs
    let email = document.getElementById('email').value.trim();
    let password = document.getElementById('password').value.trim();

    let isValid = true;

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
        alert('Login successful!');
        window.location.href = "index.html";
    }
});

// Email validation function
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(String(email).toLowerCase());
}

// Redirect to sign up page if the "Sign Up" button is clicked
document.getElementById('signupFormRedirect').addEventListener('submit', function(e) {
    e.preventDefault();
    window.location.href = "signup.html"; // Change to the actual sign-up page location
});
// Handle login form submission
document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault(); // Prevent form submission
    
    // Redirect to login.html
    window.location.href = "login_signup.html";
});
