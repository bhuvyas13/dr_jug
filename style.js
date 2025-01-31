// Select the title element
const title = document.getElementById('animated-title');
const letters = title.querySelectorAll('span span');

// Function to start the zoom-out animation
function startZoomOut() {
    title.style.transform = 'scale(1)'; // Zoom out to normal size
}

// Function to trigger the liquid transition
function startLiquidTransition() {
    letters.forEach((letter, index) => {
        letter.style.animationDelay = `${index * 0.1}s`; // Stagger the animation delay
        letter.classList.add('liquid');
    });
}

// Start zoom-out effect after the page loads
window.onload = function() {
    // Start zoom-out animation
    setTimeout(startZoomOut, 100);

    // Trigger liquid effect after zoom animation (1.5s delay)
    setTimeout(startLiquidTransition, 1600);
};

// Add the "liquid" class to the title element to trigger the animation
document.getElementById("animated-title").classList.add("liquid");
