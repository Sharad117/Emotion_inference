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
    window.location.href = "login-page.html";
}






