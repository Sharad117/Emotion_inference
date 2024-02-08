function startSpeechRecognition() {
    const recognition = new webkitSpeechRecognition() || new SpeechRecognition();

    recognition.onresult = function (event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById('voiceInput').value = transcript;
        document.getElementById('textOutput').value = "You said: " + transcript;
    };

    recognition.onend = function () {
        console.log('Speech recognition ended.');
    };

    recognition.start();
}
