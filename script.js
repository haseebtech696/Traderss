/**
 * MALIK TRADERS - JAVASCRIPT
 * Plain vanilla JS for interactive navigation, category filters,
 * minimal scroll animations, and UI-only contact form validation.
 */

document.addEventListener('DOMContentLoaded', () => {
  initMobileNav();
  initScrollAnimations();
  initProductFilter();
  initContactForm();
  initYear();
});

function initYear() {
  const yearEl = document.getElementById('current-year');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
}

/* --------------------------------------------------------------------------
   1. Mobile Navigation Toggle
   -------------------------------------------------------------------------- */
function initMobileNav() {
  const toggleBtn = document.querySelector('.nav-toggle');
  const navMenu = document.querySelector('.nav-menu');

  if (!toggleBtn || !navMenu) return;

  toggleBtn.addEventListener('click', (e) => {
    e.stopPropagation();
    const isOpen = toggleBtn.classList.toggle('open');
    navMenu.classList.toggle('open');
    toggleBtn.setAttribute('aria-expanded', isOpen ? 'true' : 'false');
  });

  // Close nav when clicking a menu link
  const navLinks = navMenu.querySelectorAll('.nav-link');
  navLinks.forEach((link) => {
    link.addEventListener('click', () => {
      toggleBtn.classList.remove('open');
      navMenu.classList.remove('open');
      toggleBtn.setAttribute('aria-expanded', 'false');
    });
  });

  // Close nav when clicking outside
  document.addEventListener('click', (e) => {
    if (!navMenu.contains(e.target) && !toggleBtn.contains(e.target)) {
      toggleBtn.classList.remove('open');
      navMenu.classList.remove('open');
      toggleBtn.setAttribute('aria-expanded', 'false');
    }
  });
}

/* --------------------------------------------------------------------------
   2. Scroll Animations (IntersectionObserver)
   Soft fade/slide-up when sections scroll into view
   -------------------------------------------------------------------------- */
function initScrollAnimations() {
  const revealElements = document.querySelectorAll('.reveal');

  if (!revealElements.length) return;

  // Use IntersectionObserver if supported
  if ('IntersectionObserver' in window) {
    const observerOptions = {
      root: null,
      rootMargin: '0px 0px -40px 0px',
      threshold: 0.12,
    };

    const revealObserver = new IntersectionObserver((entries, observer) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          // Once animated, no need to observe again
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    revealElements.forEach((el) => revealObserver.observe(el));
  } else {
    // Fallback for older browsers
    revealElements.forEach((el) => el.classList.add('is-visible'));
  }
}

/* --------------------------------------------------------------------------
   3. Product Category Filter (Products Page)
   -------------------------------------------------------------------------- */
function initProductFilter() {
  const filterBtns = document.querySelectorAll('.filter-btn');
  const productCards = document.querySelectorAll('.product-card[data-category]');
  const countEl = document.getElementById('product-count');

  if (!filterBtns.length || !productCards.length) return;

  filterBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      // Update active button state
      filterBtns.forEach((b) => b.classList.remove('active'));
      btn.classList.add('active');

      const filterCategory = btn.getAttribute('data-filter');
      let visibleCount = 0;

      productCards.forEach((card) => {
        const itemCategory = card.getAttribute('data-category');
        const matches = filterCategory === 'all' || itemCategory === filterCategory;

        if (matches) {
          card.style.display = 'flex';
          // Trigger slight reflow for smooth appearance
          requestAnimationFrame(() => {
            card.style.opacity = '1';
            card.style.transform = 'translateY(0)';
          });
          visibleCount++;
        } else {
          card.style.display = 'none';
          card.style.opacity = '0';
          card.style.transform = 'translateY(10px)';
        }
      });

      // Update counter text if present
      if (countEl) {
        countEl.textContent = `Showing ${visibleCount} of ${productCards.length} products`;
      }
    });
  });
}

/* --------------------------------------------------------------------------
   4. Contact Form Validation (UI-only, no backend)
   -------------------------------------------------------------------------- */
function initContactForm() {
  const contactForm = document.getElementById('contact-form');
  const successBanner = document.getElementById('form-success-banner');

  if (!contactForm) return;

  const nameInput = document.getElementById('user-name');
  const phoneInput = document.getElementById('user-phone');
  const messageInput = document.getElementById('user-message');

  const nameError = document.getElementById('name-error');
  const phoneError = document.getElementById('phone-error');
  const messageError = document.getElementById('message-error');

  // Helper to reset error state
  function clearErrors() {
    [nameInput, phoneInput, messageInput].forEach((input) => {
      if (input) input.classList.remove('error');
    });
    [nameError, phoneError, messageError].forEach((err) => {
      if (err) err.classList.remove('visible');
    });
  }

  // Clear errors on input
  [nameInput, phoneInput, messageInput].forEach((input) => {
    if (!input) return;
    input.addEventListener('input', () => {
      input.classList.remove('error');
      const errEl = document.getElementById(`${input.id.replace('user-', '')}-error`);
      if (errEl) errEl.classList.remove('visible');
    });
  });

  contactForm.addEventListener('submit', (e) => {
    e.preventDefault();
    clearErrors();

    let isValid = true;

    // Validate Name
    const nameVal = nameInput ? nameInput.value.trim() : '';
    if (nameVal.length < 2) {
      isValid = false;
      if (nameInput) nameInput.classList.add('error');
      if (nameError) {
        nameError.textContent = 'Please enter your full name (minimum 2 characters).';
        nameError.classList.add('visible');
      }
    }

    // Validate Phone (digits, spaces, plus, hyphens allowed; min 7 digits)
    const phoneVal = phoneInput ? phoneInput.value.trim() : '';
    const phoneDigits = phoneVal.replace(/\D/g, '');
    if (phoneDigits.length < 7) {
      isValid = false;
      if (phoneInput) phoneInput.classList.add('error');
      if (phoneError) {
        phoneError.textContent = 'Please enter a valid phone number (at least 7 digits).';
        phoneError.classList.add('visible');
      }
    }

    // Validate Message
    const messageVal = messageInput ? messageInput.value.trim() : '';
    if (messageVal.length < 5) {
      isValid = false;
      if (messageInput) messageInput.classList.add('error');
      if (messageError) {
        messageError.textContent = 'Please enter your message or product query (at least 5 characters).';
        messageError.classList.add('visible');
      }
    }

    if (!isValid) {
      // Focus first erroneous input
      const firstError = contactForm.querySelector('.form-input.error, .form-textarea.error');
      if (firstError) firstError.focus();
      return;
    }

    // Success State (UI-only)
    if (successBanner) {
      successBanner.classList.add('visible');
      successBanner.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
    }

    // Reset form
    contactForm.reset();
  });
}
