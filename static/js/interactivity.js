document.addEventListener('DOMContentLoaded', function() {
    // Form validation example

    document.addEventListener('DOMContentLoaded', function() {
        const modal = document.getElementById('gallery-modal');
        const modalImage = document.getElementById('modal-image');
        const closeBtn = document.querySelector('.close');
    
        document.querySelectorAll('.gallery-item').forEach(item => {
            item.addEventListener('click', () => {
                const imageUrl = item.getAttribute('data-image');
                modalImage.src = imageUrl;
                modal.style.display = 'flex';
            });
        });
    
        closeBtn.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    
        modal.addEventListener('click', (e) => {
            if (e.target !== modalImage) {
                modal.style.display = 'none';
            }
        });
    });
    

    const form = document.querySelector('form');
    form.addEventListener('submit', function(event) {
        const distance = document.getElementById('distance').value;
        const fuelEfficiency = document.getElementById('fuel_efficiency').value;
        
        if (distance <= 0 || fuelEfficiency <= 0) {
            event.preventDefault();
            alert('Please enter valid values for distance and fuel efficiency.');
        }
    });

    // Button hover effect example
    const buttons = document.querySelectorAll('.btn');
    buttons.forEach(button => {
        button.addEventListener('mouseenter', () => {
            button.style.backgroundColor = '#388E3C';
        });
        button.addEventListener('mouseleave', () => {
            button.style.backgroundColor = '#4CAF50';
        });
    });
});
