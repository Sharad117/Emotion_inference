var smart = document.getElementsByClassName('smart')
document.addEventListener("DOMContentLoaded", function () {
    const menuIcon = document.querySelector(".menu-icon");
    const nav = document.querySelector("nav");

    menuIcon.addEventListener("click", function () {
        nav.classList.toggle("show");
    });
});


const menuIcon = document.getElementById('menuIcon');
const bars = document.querySelectorAll('.menu-icon .bar');
let isRotated = false;

menuIcon.addEventListener('click', () => {
    isRotated = !isRotated;

    // Rotate each bar element and adjust position to form close icon
    gsap.to(bars[0], { rotation: isRotated ? 45 : 0, y: isRotated ? 8 : 0, ease: 'power1.inOut' });
    gsap.to(bars[1], { opacity: isRotated ? 0 : 1, ease: 'power1.inOut' });
    gsap.to(bars[2], { rotation: isRotated ? -45 : 0, y: isRotated ? -8 : 0, ease: 'power1.inOut' });

    

});

function openNewPage(){
    window.location.href = "Frontend/HTML/dashboard.html";
}

function startSpeechRecognition() {
    const recognition = new (webkitSpeechRecognition || SpeechRecognition)();

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

// ****************************MAP*******************************************
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -34.397, lng: 150.644},
    zoom: 8
  });
  google.maps.event.addDomListener(document.getElementById('btn'), 'click', function() {
    randomBetween();
  })
}
    function randomBetween() {
      var random = new google.maps.LatLng( (Math.random()*(85*2)-85), (Math.random()*(180*2)-180) );
      var marker = new google.maps.Marker({
        map: map,
        position: random
      });
      map.setCenter(marker.getPosition());
    }

// ****************************************************************************
