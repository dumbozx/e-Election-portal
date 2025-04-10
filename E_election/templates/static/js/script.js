// General Site-wide JavaScript

console.log("E-Election Portal JS Loaded");

// Example: Add confirmation to delete buttons (if you add them)
document.addEventListener('DOMContentLoaded', function() {
    const deleteButtons = document.querySelectorAll('.btn-delete-confirm'); // Add this class to delete buttons

    deleteButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const message = button.getAttribute('data-confirm-message') || 'Are you sure you want to delete this item? This action cannot be undone.';
            if (!confirm(message)) {
                event.preventDefault(); // Stop the default action (e.g., form submission or link navigation)
            }
        });
    });

    // Add other general JS enhancements here
    // e.g., activate tooltips if using Bootstrap tooltips
    // var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'))
    // var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    //   return new bootstrap.Tooltip(tooltipTriggerEl)
    // })

});

// Specific function called from vote.html (already included there, but could be here)
// function confirmVote() { ... }