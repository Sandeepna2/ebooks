// Books and Authors Data Store + Cart Manager

export const booksData = [
  {
    id: "1",
    title: "The Enchanted Forest",
    author: "Emily Winters",
    authorId: "1",
    price: 19.99,
    category: "Fantasy",
    rating: 4.8,
    reviewsCount: 124,
    description: "In a realm where magic thrives, a young girl named Clara stumbles upon an ancient forest filled with mythical creatures and hidden wonders.",
    image: "./assets/images/book1.jpg"
  },
  {
    id: "2",
    title: "Shadows of the Past",
    author: "Sarah Larkin",
    authorId: "2",
    price: 15.99,
    category: "Mystery",
    rating: 4.6,
    reviewsCount: 89,
    description: "Detective Mark Thompson is drawn into a web of intrigue when a series of disappearances rock his small town.",
    image: "./assets/images/book-2.jpg"
  },
  {
    id: "3",
    title: "Whispers of the Ocean",
    author: "James Holloway",
    authorId: "3",
    price: 25.99,
    category: "Romance",
    rating: 4.9,
    reviewsCount: 215,
    description: "Marine biologist Mia Carter returns to her coastal hometown to study dolphins, but she finds more than just research opportunities.",
    image: "./assets/images/book-3.jpg"
  },
  {
    id: "4",
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald",
    authorId: "4",
    price: 12.99,
    category: "Classic",
    rating: 4.7,
    reviewsCount: 340,
    description: "A story of ambition, love, and tragedy set in the Roaring Twenties on Long Island.",
    image: "https://images.unsplash.com/photo-1544947950-fa07a98d237f?auto=format&fit=crop&w=600&q=80"
  },
  {
    id: "5",
    title: "To Kill a Mockingbird",
    author: "Harper Lee",
    authorId: "5",
    price: 14.99,
    category: "Classic",
    rating: 4.9,
    reviewsCount: 450,
    description: "A gripping, heart-wrenching story of racial injustice and the loss of innocence in the American South.",
    image: "https://images.unsplash.com/photo-1512820790803-83ca734da794?auto=format&fit=crop&w=600&q=80"
  },
  {
    id: "6",
    title: "1984 - Dystopian Reality",
    author: "George Orwell",
    authorId: "6",
    price: 18.50,
    category: "Sci-Fi",
    rating: 4.8,
    reviewsCount: 512,
    description: "A cautionary tale of totalitarianism, mass surveillance, and repressive regimentation of personhood.",
    image: "https://images.unsplash.com/photo-1543002588-bfa74002ed7e?auto=format&fit=crop&w=600&q=80"
  },
  {
    id: "7",
    title: "Pride and Prejudice",
    author: "Jane Austen",
    authorId: "7",
    price: 11.99,
    category: "Romance",
    rating: 4.8,
    reviewsCount: 290,
    description: "A classic romantic novel following Elizabeth Bennet as she deals with issues of manners, upbringing, and marriage.",
    image: "https://images.unsplash.com/photo-1497633762265-9d179a990aa6?auto=format&fit=crop&w=600&q=80"
  },
  {
    id: "8",
    title: "The Catcher in the Rye",
    author: "J.D. Salinger",
    authorId: "8",
    price: 16.75,
    category: "Fiction",
    rating: 4.5,
    reviewsCount: 180,
    description: "A story about teenage angst and alienation narrated by the iconic protagonist Holden Caulfield.",
    image: "https://images.unsplash.com/photo-1532012197267-da84d127e765?auto=format&fit=crop&w=600&q=80"
  }
];

export const authorsData = [
  {
    id: "1",
    name: "Emily Winters",
    genre: "Fantasy & Fiction",
    bio: "Emily Winters is a bestselling fantasy novelist known for her rich world-building and enchanted storytelling.",
    image: "https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&w=300&q=80",
    booksCount: 12
  },
  {
    id: "2",
    name: "Sarah Larkin",
    genre: "Mystery & Thriller",
    bio: "Sarah Larkin spent ten years as a crime reporter before writing award-winning suspense novels.",
    image: "https://images.unsplash.com/photo-1580489944761-15a19d654956?auto=format&fit=crop&w=300&q=80",
    booksCount: 8
  },
  {
    id: "3",
    name: "James Holloway",
    genre: "Romance & Drama",
    bio: "James Holloway writes ocean-themed modern romance novels inspired by his travels around the world.",
    image: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?auto=format&fit=crop&w=300&q=80",
    booksCount: 15
  },
  {
    id: "4",
    name: "F. Scott Fitzgerald",
    genre: "Classic Literature",
    bio: "American novelist widely regarded as one of the greatest writers of the 20th century.",
    image: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?auto=format&fit=crop&w=300&q=80",
    booksCount: 5
  },
  {
    id: "5",
    name: "Harper Lee",
    genre: "Classic Fiction",
    bio: "American novelist best known for her 1960 Pulitzer Prize-winning novel To Kill a Mockingbird.",
    image: "https://images.unsplash.com/photo-1544005313-94ddf0286df2?auto=format&fit=crop&w=300&q=80",
    booksCount: 2
  },
  {
    id: "6",
    name: "George Orwell",
    genre: "Dystopian Sci-Fi",
    bio: "English novelist and essayist whose work is characterized by lucid prose and opposition to totalitarianism.",
    image: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?auto=format&fit=crop&w=300&q=80",
    booksCount: 6
  },
  {
    id: "7",
    name: "Jane Austen",
    genre: "Romantic Fiction",
    bio: "English novelist known primarily for her six major novels interpreting the British landed gentry.",
    image: "https://images.unsplash.com/photo-1573496359142-b8d87734a5a2?auto=format&fit=crop&w=300&q=80",
    booksCount: 6
  },
  {
    id: "8",
    name: "J.D. Salinger",
    genre: "Modern Fiction",
    bio: "American writer known for his novel The Catcher in the Rye and his reclusive nature.",
    image: "https://images.unsplash.com/photo-1519085360753-af0119f7cbe7?auto=format&fit=crop&w=300&q=80",
    booksCount: 4
  }
];

// --- Cart Manager ---

export function getCart() {
  try {
    return JSON.parse(localStorage.getItem('ebooks_cart') || '[]');
  } catch (e) {
    return [];
  }
}

export function saveCart(cart) {
  localStorage.setItem('ebooks_cart', JSON.stringify(cart));
  updateCartBadge();
}

export function addToCart(bookId, quantity = 1) {
  const cart = getCart();
  const existingItem = cart.find(item => item.id === String(bookId));
  const book = booksData.find(b => b.id === String(bookId));
  if (!book) return false;

  if (existingItem) {
    existingItem.quantity += quantity;
  } else {
    cart.push({
      id: book.id,
      title: book.title,
      author: book.author,
      price: book.price,
      image: book.image,
      quantity: quantity
    });
  }
  saveCart(cart);
  showToast(`Added "${book.title}" to cart!`);
  return true;
}

export function removeFromCart(bookId) {
  let cart = getCart();
  cart = cart.filter(item => item.id !== String(bookId));
  saveCart(cart);
}

export function updateCartQty(bookId, quantity) {
  const cart = getCart();
  const item = cart.find(i => i.id === String(bookId));
  if (item) {
    item.quantity = Math.max(1, quantity);
    saveCart(cart);
  }
}

export function getCartCount() {
  const cart = getCart();
  return cart.reduce((total, item) => total + item.quantity, 0);
}

export function updateCartBadge() {
  const badgeElements = document.querySelectorAll('.cart-badge-count');
  const count = getCartCount();
  badgeElements.forEach(badge => {
    badge.textContent = count;
    badge.style.display = count > 0 ? 'inline-block' : 'none';
  });
}

export function showToast(message, type = 'success') {
  let toastContainer = document.getElementById('toast-container');
  if (!toastContainer) {
    toastContainer = document.createElement('div');
    toastContainer.id = 'toast-container';
    toastContainer.style.position = 'fixed';
    toastContainer.style.bottom = '20px';
    toastContainer.style.right = '20px';
    toastContainer.style.zIndex = '9999';
    document.body.appendChild(toastContainer);
  }

  const toast = document.createElement('div');
  toast.className = `alert alert-${type} alert-dismissible fade show shadow-lg`;
  toast.style.minWidth = '280px';
  toast.style.borderRadius = '10px';
  toast.innerHTML = `
    <div class="d-flex align-items-center">
      <i class="fas ${type === 'success' ? 'fa-check-circle' : 'fa-info-circle'} me-2 fs-5"></i>
      <div>${message}</div>
    </div>
  `;
  toastContainer.appendChild(toast);

  setTimeout(() => {
    toast.classList.remove('show');
    setTimeout(() => toast.remove(), 300);
  }, 3000);
}
