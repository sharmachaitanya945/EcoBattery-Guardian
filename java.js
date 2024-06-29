const navToggle = document.querySelector('.fas.fa-bars');
const navMenu = document.querySelector('.navbar ul');

navToggle.addEventListener('click', () => {
    navMenu.classList.toggle('show');
});


let slideIndex = 0;
const slides = document.querySelectorAll('.slide');

function showSlides() {
    slides.forEach(slide => slide.style.display = 'none');
    slideIndex++;
    if (slideIndex > slides.length) slideIndex = 1;
    slides[slideIndex - 1].style.display = 'block';
    setTimeout(showSlides, 3000); // Change image every 3 seconds
}

showSlides();


const form = document.querySelector('form');

form.addEventListener('submit', (event) => {
    const name = document.querySelector('input[type="text"]').value;
    const email = document.querySelector('input[type="email"]').value;
    const phone = document.querySelector('input[type="tel"]').value;
    const message = document.querySelector('textarea').value;

    if (!name || !email || !phone || !message) {
        alert('Please fill in all fields.');
        event.preventDefault(); // Prevent form submission if fields are empty
    }
});


document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function(e) {
        e.preventDefault();

        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});
