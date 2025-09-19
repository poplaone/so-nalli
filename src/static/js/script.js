/**
 * Student Management System - JavaScript Functions
 * NIELIT Project by [Student Name]
 */

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
});

/**
 * Initialize application
 */
function initializeApp() {
    // Initialize tooltips
    initializeTooltips();
    
    // Initialize form validation
    initializeFormValidation();
    
    // Initialize table features
    initializeTableFeatures();
    
    // Initialize alerts auto-dismiss
    initializeAlerts();
    
    console.log('Student Management System initialized successfully');
}

/**
 * Initialize Bootstrap tooltips
 */
function initializeTooltips() {
    var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

/**
 * Initialize form validation
 */
function initializeFormValidation() {
    // Get all forms with validation
    const forms = document.querySelectorAll('.needs-validation');
    
    // Loop over forms and prevent submission
    Array.prototype.slice.call(forms).forEach(function(form) {
        form.addEventListener('submit', function(event) {
            if (!form.checkValidity()) {
                event.preventDefault();
                event.stopPropagation();
            }
            form.classList.add('was-validated');
        }, false);
    });
    
    // Email validation
    const emailInputs = document.querySelectorAll('input[type="email"]');
    emailInputs.forEach(function(input) {
        input.addEventListener('blur', function() {
            validateEmail(this);
        });
    });
    
    // Phone validation
    const phoneInputs = document.querySelectorAll('input[type="tel"]');
    phoneInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            formatPhoneNumber(this);
        });
    });
}

/**
 * Validate email format
 */
function validateEmail(input) {
    const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    const isValid = emailRegex.test(input.value);
    
    if (input.value && !isValid) {
        input.setCustomValidity('Please enter a valid email address');
        input.classList.add('is-invalid');
    } else {
        input.setCustomValidity('');
        input.classList.remove('is-invalid');
    }
}

/**
 * Format phone number input
 */
function formatPhoneNumber(input) {
    // Remove all non-digit characters
    let value = input.value.replace(/\D/g, '');
    
    // Limit to 10 digits
    if (value.length > 10) {
        value = value.slice(0, 10);
    }
    
    // Format as (XXX) XXX-XXXX
    if (value.length >= 6) {
        value = `(${value.slice(0, 3)}) ${value.slice(3, 6)}-${value.slice(6)}`;
    } else if (value.length >= 3) {
        value = `(${value.slice(0, 3)}) ${value.slice(3)}`;
    }
    
    input.value = value;
}

/**
 * Initialize table features
 */
function initializeTableFeatures() {
    // Add search functionality to tables
    addTableSearch();
    
    // Add sorting functionality
    addTableSorting();
    
    // Add row highlighting
    addRowHighlighting();
}

/**
 * Add search functionality to tables
 */
function addTableSearch() {
    const tables = document.querySelectorAll('.table');
    
    tables.forEach(function(table) {
        // Create search input if it doesn't exist
        const searchContainer = table.closest('.card-body');
        if (searchContainer && !searchContainer.querySelector('.table-search')) {
            const searchInput = document.createElement('input');
            searchInput.type = 'text';
            searchInput.className = 'form-control table-search mb-3';
            searchInput.placeholder = 'Search table...';
            
            searchInput.addEventListener('input', function() {
                filterTable(table, this.value);
            });
            
            searchContainer.insertBefore(searchInput, table.parentElement);
        }
    });
}

/**
 * Filter table rows based on search term
 */
function filterTable(table, searchTerm) {
    const rows = table.querySelectorAll('tbody tr');
    const term = searchTerm.toLowerCase();
    
    rows.forEach(function(row) {
        const text = row.textContent.toLowerCase();
        const shouldShow = text.includes(term);
        row.style.display = shouldShow ? '' : 'none';
    });
}

/**
 * Add sorting functionality to tables
 */
function addTableSorting() {
    const tables = document.querySelectorAll('.table');
    
    tables.forEach(function(table) {
        const headers = table.querySelectorAll('thead th');
        
        headers.forEach(function(header, index) {
            if (header.textContent.trim() && index < headers.length - 1) { // Skip action column
                header.style.cursor = 'pointer';
                header.title = 'Click to sort';
                
                header.addEventListener('click', function() {
                    sortTable(table, index);
                });
            }
        });
    });
}

/**
 * Sort table by column
 */
function sortTable(table, columnIndex) {
    const tbody = table.querySelector('tbody');
    const rows = Array.from(tbody.querySelectorAll('tr'));
    
    // Determine sort direction
    const isAscending = !table.dataset.sortAsc || table.dataset.sortAsc === 'false';
    table.dataset.sortAsc = isAscending;
    
    // Sort rows
    rows.sort(function(a, b) {
        const aText = a.cells[columnIndex].textContent.trim();
        const bText = b.cells[columnIndex].textContent.trim();
        
        // Try to parse as numbers
        const aNum = parseFloat(aText);
        const bNum = parseFloat(bText);
        
        if (!isNaN(aNum) && !isNaN(bNum)) {
            return isAscending ? aNum - bNum : bNum - aNum;
        } else {
            return isAscending ? 
                aText.localeCompare(bText) : 
                bText.localeCompare(aText);
        }
    });
    
    // Reorder rows in DOM
    rows.forEach(function(row) {
        tbody.appendChild(row);
    });
}

/**
 * Add row highlighting on hover
 */
function addRowHighlighting() {
    const tables = document.querySelectorAll('.table-hover');
    
    tables.forEach(function(table) {
        const rows = table.querySelectorAll('tbody tr');
        
        rows.forEach(function(row) {
            row.addEventListener('mouseenter', function() {
                this.style.backgroundColor = 'rgba(0, 123, 255, 0.1)';
            });
            
            row.addEventListener('mouseleave', function() {
                this.style.backgroundColor = '';
            });
        });
    });
}

/**
 * Initialize alerts auto-dismiss
 */
function initializeAlerts() {
    const alerts = document.querySelectorAll('.alert:not(.alert-permanent)');
    
    alerts.forEach(function(alert) {
        // Auto-dismiss after 5 seconds
        setTimeout(function() {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000);
    });
}

/**
 * Confirm deletion
 */
function confirmDelete(itemName, itemType) {
    return confirm(`Are you sure you want to delete this ${itemType}: ${itemName}?\n\nThis action cannot be undone.`);
}

/**
 * Show loading spinner
 */
function showLoading(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="loading"></span> Loading...';
    button.disabled = true;
    
    return function() {
        button.innerHTML = originalText;
        button.disabled = false;
    };
}

/**
 * Format date for display
 */
function formatDate(dateString) {
    if (!dateString) return 'N/A';
    
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
    });
}

/**
 * Validate form before submission
 */
function validateForm(form) {
    const requiredFields = form.querySelectorAll('[required]');
    let isValid = true;
    
    requiredFields.forEach(function(field) {
        if (!field.value.trim()) {
            field.classList.add('is-invalid');
            isValid = false;
        } else {
            field.classList.remove('is-invalid');
        }
    });
    
    return isValid;
}

/**
 * Export table to CSV
 */
function exportTableToCSV(tableId, filename) {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    let csv = [];
    const rows = table.querySelectorAll('tr');
    
    rows.forEach(function(row) {
        const cols = row.querySelectorAll('td, th');
        const rowData = [];
        
        cols.forEach(function(col, index) {
            // Skip action columns
            if (index < cols.length - 1) {
                rowData.push('"' + col.textContent.trim().replace(/"/g, '""') + '"');
            }
        });
        
        csv.push(rowData.join(','));
    });
    
    // Download CSV
    const csvContent = csv.join('\n');
    const blob = new Blob([csvContent], { type: 'text/csv' });
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename || 'export.csv';
    a.click();
    window.URL.revokeObjectURL(url);
}

/**
 * Print table
 */
function printTable(tableId) {
    const table = document.getElementById(tableId);
    if (!table) return;
    
    const printWindow = window.open('', '_blank');
    printWindow.document.write(`
        <html>
            <head>
                <title>Student Management System - Report</title>
                <style>
                    body { font-family: Arial, sans-serif; }
                    table { width: 100%; border-collapse: collapse; }
                    th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
                    th { background-color: #f2f2f2; }
                    @media print { body { margin: 0; } }
                </style>
            </head>
            <body>
                <h2>Student Management System Report</h2>
                ${table.outerHTML}
            </body>
        </html>
    `);
    printWindow.document.close();
    printWindow.print();
}

// Global utility functions
window.SMS = {
    confirmDelete: confirmDelete,
    showLoading: showLoading,
    formatDate: formatDate,
    validateForm: validateForm,
    exportTableToCSV: exportTableToCSV,
    printTable: printTable
};