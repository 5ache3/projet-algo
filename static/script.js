// Minimal JavaScript - only for form validation and UX enhancements

// Handle Enter key in form inputs
document.addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && e.target.tagName === 'INPUT') {
        e.preventDefault();
        // Find the form and submit it
        const form = e.target.closest('form');
        if (form) {
            form.submit();
        }
    }
});

// Form validation
document.addEventListener('DOMContentLoaded', function () {
    const addForm = document.getElementById('addForm');

    if (addForm) {
        addForm.addEventListener('submit', function (e) {
            const priority = document.getElementById('priority').value;
            const weight = document.getElementById('weight').value;

            if (priority < 1 || priority > 5) {
                e.preventDefault();
                alert('La priorité doit être entre 1 et 5');
                return false;
            }

            if (weight <= 0) {
                e.preventDefault();
                alert('Le poids doit être supérieur à 0');
                return false;
            }
        });
    }
});

// Auto-hide flash messages after 5 seconds
setTimeout(function () {
    const flashMessages = document.querySelectorAll('[class*="border-l-4"]');
    flashMessages.forEach(function (msg) {
        if (msg.parentElement.classList.contains('mb-6')) {
            msg.style.transition = 'opacity 0.5s';
            msg.style.opacity = '0';
            setTimeout(function () {
                msg.remove();
            }, 500);
        }
    });
}, 5000);