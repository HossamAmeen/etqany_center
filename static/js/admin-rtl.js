// Add this to ensure "Dashboard" text is replaced in sidebar
document.addEventListener('DOMContentLoaded', function() {
    if (document.documentElement.dir === 'rtl' || document.documentElement.getAttribute('dir') === 'rtl') {
        // Replace Dashboard text in sidebar
        const navLinks = document.querySelectorAll('.nav-sidebar .nav-link');
        navLinks.forEach(link => {
            if (link.textContent.trim() === 'Dashboard' || 
                link.textContent.includes('Dashboard')) {
                link.innerHTML = link.innerHTML.replace(/Dashboard/gi, 'لوحة التحكم');
            }
        });
        
        // Replace Services if needed
        const servicesLinks = document.querySelectorAll('.nav-sidebar .nav-link');
        servicesLinks.forEach(link => {
            if (link.textContent.trim() === 'Services') {
                link.innerHTML = link.innerHTML.replace(/Services/gi, 'خدمات');
            }
        });
    }
});