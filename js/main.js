// Add scroll behavior to navbar
window.addEventListener('scroll', function() {
    const navbar = document.querySelector('.navbar');
    if (window.scrollY > 50) {
        navbar.style.padding = '0.5rem 1rem';
        navbar.style.backgroundColor = '#0a1a2f';
    } else {
        navbar.style.padding = '1rem';
        navbar.style.backgroundColor = '#1d3557';
    }
});

// Initialize tooltips
document.addEventListener('DOMContentLoaded', function() {
    // You can add more JavaScript functionality here
    console.log('Boxing Bootcamp website loaded!');
}); 