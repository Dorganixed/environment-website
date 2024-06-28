document.addEventListener('DOMContentLoaded', function() {
    let carouselInner = document.querySelector('.carousel-inner');
    let items = document.querySelectorAll('.carousel-item');
    let currentIndex = 0;

    setInterval(() => {
        items[currentIndex].classList.remove('active');
        currentIndex = (currentIndex + 1) % items.length;
        items[currentIndex].classList.add('active');
        carouselInner.style.transform = `translateX(-${currentIndex * 100}%)`;
    }, 3000);
});
