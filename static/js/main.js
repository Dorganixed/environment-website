// Carousel
let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("carousel-slide");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) {
        slideIndex = 1;
    }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 3000); // Her 3 saniyede bir görsel değiştir
}

// Gallery Modal
let galleryItems = document.querySelectorAll('.gallery-item');
let modal = document.getElementById('gallery-modal');
let modalImg = document.getElementById('modal-image');
let closeModal = document.getElementsByClassName('close')[0];

galleryItems.forEach(item => {
    item.addEventListener('click', function () {
        modal.style.display = "block";
        modalImg.src = this.getAttribute('data-image');
    });
});

closeModal.onclick = function () {
    modal.style.display = "none";
}

// Dışarı tıklayınca modalı kapatma
window.onclick = function (event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}
