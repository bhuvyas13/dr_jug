// Function to open different emotion pages
function openEmotionPage(emotion) {
    let emotionPageUrl = '';
    switch (emotion) {
        case 'joy':
            emotionPageUrl = 'joy.html';
            break;
        case 'sadness':
            emotionPageUrl = 'sadness.html';
            break;
        case 'anger':
            emotionPageUrl = 'anger.html';
            break;
        case 'disgust':
            emotionPageUrl = 'disgust.html';
            break;
        case 'fear':
            emotionPageUrl = 'fear.html';
            break;
    }
    window.location.href = emotionPageUrl;
}
function openEmotionPage(emotion) {
    alert("You selected: " + emotion + ". Here, you would navigate to the relevant content about managing this emotion.");
    // Here you can redirect to another page or display relevant content
}
