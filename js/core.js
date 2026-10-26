/**
 * UI & UX ENHANCEMENTS
 * Handles navigation, modals, and environment-specific adjustments.
 */
document.addEventListener('DOMContentLoaded', function () {
    // Mobile detection (Handled inline in head to prevent jitter)

    // Header scroll effect
    const header = document.querySelector('.main-header');
    if (header) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 50) header.classList.add('scrolled');
            else header.classList.remove('scrolled');
        });
    }

    // Mobile Menu Toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    if (menuToggle && mainNav) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            mainNav.classList.toggle('active');
            document.body.style.overflow = mainNav.classList.contains('active') ? 'hidden' : '';
        });

        const navLinks = mainNav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                mainNav.classList.remove('active');
                document.body.style.overflow = '';
            });
        });
    }

    // Shared Modal Logic (Media, Case Studies, Contact)
    const setupModal = (triggerClass, modalId, closeId, updateFn) => {
        const modal = document.getElementById(modalId);
        const triggers = document.querySelectorAll(triggerClass);
        const closeBtn = document.getElementById(closeId);

        if (!modal || !closeBtn) return;

        triggers.forEach(trigger => {
            trigger.addEventListener('click', () => {
                if (updateFn) updateFn(trigger, modal);
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        });

        const closeModal = () => {
            modal.classList.remove('active');
            if (!document.querySelector('.modal-overlay.active')) {
                document.body.style.overflow = '';
            }
        };

        closeBtn.addEventListener('click', closeModal);
        modal.addEventListener('click', (e) => {
            if (e.target === modal) closeModal();
        });
    };

    // Initialize Modals
    setupModal('.media-item', 'mediaModal', 'closeModal', (item) => {
        document.getElementById('modalTitle').textContent = item.getAttribute('data-title');
        document.getElementById('modalDesc').textContent = item.getAttribute('data-desc');
        document.getElementById('modalImage').src = item.getAttribute('data-image');
        document.getElementById('modalLink').href = item.getAttribute('data-link');
        document.getElementById('modalLink').textContent = item.getAttribute('data-cta');
    });

    setupModal('.case-study-card', 'caseStudyModal', 'closeCaseStudyModal', (card) => {
        document.getElementById('csModalTag').textContent = card.getAttribute('data-tag');
        document.getElementById('csModalTitle').textContent = card.getAttribute('data-title');
        document.getElementById('csModalBody').innerHTML = card.getAttribute('data-body');
        document.getElementById('csModalResult').textContent = card.getAttribute('data-result');
    });

    setupModal('#openContactModal', 'contactModal', 'closeContactModal');
    setupModal('#mediaContactBtn', 'contactModal', 'closeContactModal');

    // ESC key support
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            document.querySelectorAll('.modal-overlay.active').forEach(m => m.classList.remove('active'));
            document.body.style.overflow = '';
        }
    });

    // Contact Form Submission
    const contactForm = document.getElementById('contactForm');
    if (contactForm) {
        contactForm.addEventListener('submit', async (e) => {
            e.preventDefault();
            const status = document.getElementById('contactStatus');
            const submit = document.getElementById('contactSubmit');
            submit.disabled = true;
            submit.textContent = 'Sending...';

            try {
                const response = await fetch(contactForm.action, {
                    method: contactForm.method,
                    body: new FormData(contactForm),
                    headers: { 'Accept': 'application/json' }
                });

                if (response.ok) {
                    status.innerHTML = "Success! Message received.";
                    status.style.display = 'block';
                    contactForm.reset();
                    setTimeout(() => { 
                        document.getElementById('contactModal').classList.remove('active');
                        document.body.style.overflow = '';
                        status.style.display = 'none';
                        submit.disabled = false;
                        submit.textContent = 'Send Message';
                    }, 3000);
                } else {
                    throw new Error('Submission failed');
                }
            } catch (error) {
                status.innerHTML = "Error. Please try again.";
                status.style.display = 'block';
                submit.disabled = false;
                submit.textContent = 'Send Message';
            }
        });
    }
});
