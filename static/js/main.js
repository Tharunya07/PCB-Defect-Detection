// Main JavaScript for PCB Defect Detection Demo

document.addEventListener('DOMContentLoaded', function() {
    // File upload preview
    const fileInput = document.getElementById('file');
    if (fileInput) {
        fileInput.addEventListener('change', function(e) {
            const fileName = e.target.files[0]?.name;
            if (fileName) {
                // Create a toast or notification to show the selected file
                showToast(`Selected file: ${fileName}`, 'info');
            }
        });
    }
    
    // Initialize tooltips and popovers if using Bootstrap
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
    
    const popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'));
    popoverTriggerList.map(function (popoverTriggerEl) {
        return new bootstrap.Popover(popoverTriggerEl);
    });
});

// Function to show a toast/notification
function showToast(message, type = 'info') {
    // Check if the toast container exists, create if it doesn't
    let toastContainer = document.querySelector('.toast-container');
    if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.className = 'toast-container position-fixed top-0 end-0 p-3';
        document.body.appendChild(toastContainer);
    }
    
    // Create the toast element
    const toastId = 'toast-' + Date.now();
    const toast = document.createElement('div');
    toast.className = `toast align-items-center text-white bg-${type} border-0`;
    toast.id = toastId;
    toast.setAttribute('role', 'alert');
    toast.setAttribute('aria-live', 'assertive');
    toast.setAttribute('aria-atomic', 'true');
    
    // Create toast content
    toast.innerHTML = `
        <div class="d-flex">
            <div class="toast-body">
                ${message}
            </div>
            <button type="button" class="btn-close btn-close-white me-2 m-auto" data-bs-dismiss="toast" aria-label="Close"></button>
        </div>
    `;
    
    // Append toast to container
    toastContainer.appendChild(toast);
    
    // Initialize and show the toast
    const toastInstance = new bootstrap.Toast(toast);
    toastInstance.show();
    
    // Remove toast after it's hidden
    toast.addEventListener('hidden.bs.toast', function() {
        toast.remove();
    });
}

// Function to handle the loading state when analyzing an image
function setLoadingState(isLoading) {
    const submitButton = document.querySelector('button[type="submit"]');
    if (!submitButton) return;
    
    if (isLoading) {
        submitButton.innerHTML = '<span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span> Analyzing...';
        submitButton.disabled = true;
    } else {
        submitButton.innerHTML = 'Analyze PCB';
        submitButton.disabled = false;
    }
}

// Add form submit event listener to show loading state
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', function() {
            setLoadingState(true);
        });
    }
});