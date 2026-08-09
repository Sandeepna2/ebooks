// Main Application JavaScript

import * as bootstrap from 'bootstrap';
import { booksData, authorsData, addToCart, getCart, removeFromCart, updateCartQty, updateCartBadge, showToast } from './booksData.js';

document.addEventListener('DOMContentLoaded', () => {
  // Initialize Cart Badge
  updateCartBadge();

  // Highlight active nav item based on current URL path
  highlightActiveNav();

  // Bind global delegated click events (Buy Now, Add to Cart, View Details)
  bindGlobalEvents();

  // Page Specific Handlers
  initHomePage();
  initBooksPage();
  initBookDetailsPage();
  initCartPage();
  initForms();
});

function highlightActiveNav() {
  const currentPath = window.location.pathname;
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .navbar-nav .btn');
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (!href) return;
    if (currentPath.endsWith(href) || (href === 'index.html' && (currentPath.endsWith('/') || currentPath.endsWith('index.html')))) {
      link.classList.add('active');
    }
  });
}

function bindGlobalEvents() {
  document.addEventListener('click', (e) => {
    // Buy / Add to Cart Button Click
    const buyBtn = e.target.closest('.btn-buy-now, .btn-add-cart');
    if (buyBtn) {
      e.preventDefault();
      const bookId = buyBtn.dataset.bookId || "1";
      addToCart(bookId);
    }
  });
}

// --- Home Page ---
function initHomePage() {
  const booksContainer = document.querySelector('.books-container');
  if (booksContainer) {
    renderBookGrid(booksContainer, booksData.slice(0, 4));
  }
}

// --- Books Listing Page ---
function initBooksPage() {
  const container = document.getElementById('all-books-container');
  const searchInput = document.getElementById('bookSearchInput');
  const categoryFilter = document.getElementById('categoryFilterSelect');

  if (container) {
    renderBookGrid(container, booksData);

    const filterBooks = () => {
      const query = searchInput ? searchInput.value.toLowerCase().trim() : '';
      const category = categoryFilter ? categoryFilter.value : '';

      const filtered = booksData.filter(book => {
        const matchesSearch = book.title.toLowerCase().includes(query) || book.author.toLowerCase().includes(query);
        const matchesCategory = category === '' || book.category === category;
        return matchesSearch && matchesCategory;
      });

      renderBookGrid(container, filtered);
    };

    if (searchInput) searchInput.addEventListener('input', filterBooks);
    if (categoryFilter) categoryFilter.addEventListener('change', filterBooks);
  }
}

function renderBookGrid(container, books) {
  if (!container) return;
  container.innerHTML = '';

  if (books.length === 0) {
    container.innerHTML = `
      <div class="col-12 text-center py-5">
        <i class="fas fa-search fa-3x text-muted mb-3"></i>
        <h4 class="text-muted">No books found</h4>
        <p>Try adjusting your search query or filter.</p>
      </div>
    `;
    return;
  }

  const detailsPath = 'book-details.html';

  books.forEach(book => {
    const col = document.createElement('div');
    col.className = 'col-md-3 mb-4';
    col.innerHTML = `
      <div class="card h-100 text-center shadow-sm hover-top transition-all">
        <div class="position-relative">
          <img src="${book.image}" alt="${book.title}" class="card-img-top book-cover-img" style="height: 240px; object-fit: cover;">
          <span class="badge bg-primary position-absolute top-0 end-0 m-2 px-2 py-1">${book.category}</span>
        </div>
        <div class="card-body d-flex flex-column">
          <h5 class="card-title text-truncate mb-1" title="${book.title}">${book.title}</h5>
          <p class="card-text text-muted small mb-2">by ${book.author}</p>
          <div class="mb-2">
            <span class="text-warning"><i class="fas fa-star"></i> ${book.rating}</span>
            <span class="text-muted small">(${book.reviewsCount})</span>
          </div>
          <h5 class="text-success mt-auto mb-3">$${book.price.toFixed(2)}</h5>
        </div>
        <div class="card-footer bg-transparent border-0 pt-0 pb-3 px-3 d-flex justify-content-between">
          <a href="${detailsPath}?id=${book.id}" class="btn btn-outline-primary btn-sm px-2">View Details</a>
          <button class="btn btn-success btn-sm btn-buy-now px-3" data-book-id="${book.id}">
            <i class="fas fa-shopping-cart me-1"></i> Buy
          </button>
        </div>
      </div>
    `;
    container.appendChild(col);
  });
}

// --- Book Details Page ---
function initBookDetailsPage() {
  const titleEl = document.getElementById('detail-book-title');
  if (!titleEl) return;

  const urlParams = new URLSearchParams(window.location.search);
  const bookId = urlParams.get('id') || "1";
  const book = booksData.find(b => b.id === bookId) || booksData[0];

  const imgEl = document.getElementById('detail-book-img');
  const authorEl = document.getElementById('detail-book-author');
  const priceEl = document.getElementById('detail-book-price');
  const descEl = document.getElementById('detail-book-desc');
  const categoryEl = document.getElementById('detail-book-category');
  const buyBtn = document.getElementById('detail-buy-btn');

  if (imgEl) imgEl.src = book.image;
  if (titleEl) titleEl.textContent = book.title;
  if (authorEl) authorEl.textContent = `Author: ${book.author}`;
  if (priceEl) priceEl.textContent = `$${book.price.toFixed(2)}`;
  if (descEl) descEl.textContent = book.description;
  if (categoryEl) categoryEl.textContent = book.category;
  if (buyBtn) {
    buyBtn.dataset.bookId = book.id;
    buyBtn.addEventListener('click', (e) => {
      e.preventDefault();
      addToCart(book.id);
    });
  }
}

// --- Cart Page ---
function initCartPage() {
  const container = document.getElementById('cartItemsContainer');
  if (!container) return;

  renderCart();
}

function renderCart() {
  const container = document.getElementById('cartItemsContainer');
  if (!container) return;

  const cart = getCart();
  const subtotalEl = document.getElementById('cartSubtotal');
  const taxEl = document.getElementById('cartTax');
  const totalEl = document.getElementById('cartTotal');
  const checkoutBtn = document.getElementById('checkoutBtn');

  if (cart.length === 0) {
    container.innerHTML = `
      <div class="card text-center py-5">
        <div class="card-body">
          <i class="fas fa-shopping-basket fa-4x text-muted mb-3"></i>
          <h3>Your cart is empty</h3>
          <p class="text-muted">Looks like you haven't added any ebooks to your cart yet.</p>
          <a href="books.html" class="btn btn-primary mt-2">Explore Books</a>
        </div>
      </div>
    `;
    if (subtotalEl) subtotalEl.textContent = '$0.00';
    if (taxEl) taxEl.textContent = '$0.00';
    if (totalEl) totalEl.textContent = '$0.00';
    if (checkoutBtn) checkoutBtn.disabled = true;
    return;
  }

  let subtotal = 0;
  container.innerHTML = '';

  cart.forEach(item => {
    const itemTotal = item.price * item.quantity;
    subtotal += itemTotal;

    const card = document.createElement('div');
    card.className = 'card mb-3 shadow-sm';
    card.innerHTML = `
      <div class="card-body">
        <div class="row align-items-center">
          <div class="col-md-2 text-center">
            <img src="${item.image}" alt="${item.title}" class="img-fluid rounded" style="max-height: 100px; object-fit: cover;">
          </div>
          <div class="col-md-5 mt-2 mt-md-0">
            <h5 class="card-title mb-1">${item.title}</h5>
            <p class="card-text text-muted small mb-2">${item.author}</p>
            <button class="btn btn-sm btn-outline-danger remove-item-btn" data-id="${item.id}">
              <i class="fas fa-trash me-1"></i> Remove
            </button>
          </div>
          <div class="col-md-3 my-2 my-md-0">
            <div class="input-group input-group-sm">
              <button class="btn btn-outline-secondary qty-minus-btn" data-id="${item.id}">-</button>
              <input type="number" class="form-control text-center qty-input" value="${item.quantity}" min="1" data-id="${item.id}">
              <button class="btn btn-outline-secondary qty-plus-btn" data-id="${item.id}">+</button>
            </div>
          </div>
          <div class="col-md-2 text-end">
            <p class="fw-bold fs-5 text-success mb-0">$${itemTotal.toFixed(2)}</p>
          </div>
        </div>
      </div>
    `;
    container.appendChild(card);
  });

  const tax = subtotal * 0.10; // 10% tax
  const total = subtotal + tax;

  if (subtotalEl) subtotalEl.textContent = `$${subtotal.toFixed(2)}`;
  if (taxEl) taxEl.textContent = `$${tax.toFixed(2)}`;
  if (totalEl) totalEl.textContent = `$${total.toFixed(2)}`;
  if (checkoutBtn) {
    checkoutBtn.disabled = false;
    checkoutBtn.onclick = () => {
      showToast('Order placed successfully! Thank you for your purchase.', 'success');
      localStorage.removeItem('ebooks_cart');
      updateCartBadge();
      setTimeout(renderCart, 1500);
    };
  }

  // Cart Event Listeners
  container.querySelectorAll('.remove-item-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      removeFromCart(btn.dataset.id);
      renderCart();
    });
  });

  container.querySelectorAll('.qty-minus-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = cart.find(i => i.id === btn.dataset.id);
      if (item && item.quantity > 1) {
        updateCartQty(btn.dataset.id, item.quantity - 1);
        renderCart();
      }
    });
  });

  container.querySelectorAll('.qty-plus-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = cart.find(i => i.id === btn.dataset.id);
      if (item) {
        updateCartQty(btn.dataset.id, item.quantity + 1);
        renderCart();
      }
    });
  });

  container.querySelectorAll('.qty-input').forEach(input => {
    input.addEventListener('change', () => {
      const val = parseInt(input.value) || 1;
      updateCartQty(input.dataset.id, val);
      renderCart();
    });
  });
}

// --- Forms Initialization ---
function initForms() {
  // Book Enquiry Form
  const enquiryForm = document.getElementById('bookEnquiryForm');
  if (enquiryForm) {
    enquiryForm.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast('Thank you! Your enquiry has been submitted successfully.', 'success');
      enquiryForm.reset();
    });
  }

  // Contact Form
  const contactForm = document.getElementById('contactForm');
  if (contactForm) {
    contactForm.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast('Message sent! We will get back to you shortly.', 'success');
      contactForm.reset();
    });
  }

  // Login Form
  const loginForm = document.getElementById('loginForm');
  if (loginForm) {
    loginForm.addEventListener('submit', (e) => {
      e.preventDefault();
      showToast('Successfully logged in!', 'success');
      setTimeout(() => { window.location.href = 'index.html'; }, 1200);
    });
  }

  // Register Form
  const registerForm = document.getElementById('registerForm');
  if (registerForm) {
    registerForm.addEventListener('submit', (e) => {
      e.preventDefault();
      const pass = document.getElementById('password') ? document.getElementById('password').value : '';
      const confirmPass = document.getElementById('confirmPassword') ? document.getElementById('confirmPassword').value : '';
      
      if (pass && confirmPass && pass !== confirmPass) {
        showToast('Passwords do not match. Please re-enter.', 'danger');
        return;
      }

      showToast('Account created successfully! Please log in.', 'success');
      setTimeout(() => { window.location.href = 'login.html'; }, 1200);
    });
  }
}
