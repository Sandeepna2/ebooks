# 📚 eBooks - Full-Stack E-Commerce Bookstore Web Application

[![Python](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.2-092E20.svg)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-3-003B57.svg)](https://www.sqlite.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3.svg)](https://getbootstrap.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E.svg)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
[![License](https://img.shields.io/badge/License-ISC-green.svg)](LICENSE)

A modern, full-stack E-Commerce digital bookstore web application built with **Python**, **Django**, **SQLite**, **Bootstrap 5**, **JavaScript**, and **Real-Time Data APIs**.

---

## ⚡ Quick One-Command Setup & Launch

Run the automated setup script to migrate database schemas, seed real books and authors into SQLite, and start the development server:

```bash
python setup.py
```
*or via NPM:*
```bash
npm run dev
```

---

## 🌟 Key Features

- 🐍 **Full-Stack Django Backend**: Robust MVC architecture utilizing Django 5.2 with ORM models for `Book`, `Author`, `Category`, `Order`, `OrderItem`, and `Enquiry`.
- 🗄️ **SQLite Relational Database**: Structured database storing real-world best-selling books, famous authors, user accounts, and purchase histories.
- ⚡ **Real-Time Data APIs**:
  - **Instant Keystroke Search (`/api/books/?q=...`)**: Dynamic live filtering of titles and authors without full page reloads.
  - **Session-Backed Cart API (`/cart/api/data/`)**: Instant cart count updates, price subtotaling, 10% digital tax calculation, and order grand totals.
  - **Live Reader Activity Ticker**: Real-time reader stats and download count indicators.
- 🔐 **User Authentication**: Complete reader registration (`/accounts/register/`), login (`/accounts/login/`), session tracking, and logout functionality using Django Auth.
- 🛒 **Shopping Cart & Checkout**: Interactive cart management (add, remove, quantity update) with checkout order processing.
- 🎨 **Modern Responsive UI**: Built with Bootstrap 5, FontAwesome icons, glassmorphism cards, toast feedback notifications, and smooth CSS transitions.

---

## 🛠️ Tech Stack

| Layer | Technology |
| :--- | :--- |
| **Backend Framework** | Python 3.14, Django 5.2 |
| **Database** | SQLite3 (`db.sqlite3`) |
| **Frontend** | HTML5, Vanilla CSS3, Bootstrap 5, JavaScript (ES6+ / Fetch API) |
| **Icons & Fonts** | FontAwesome 6, Bootstrap Icons |
| **API Format** | JSON (RESTful Django JSONResponse endpoints) |

---

## 📁 Directory Structure

```text
c:\ebooks\
├── ebooks_project/        # Django Project Root (settings, urls, wsgi)
│   ├── settings.py
│   └── urls.py
├── store/                 # Store App (Catalog, Search, Book Details, Authors, Enquiry)
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── cart/                  # Cart App (Session Cart, Checkout & Orders)
│   ├── cart.py
│   ├── context_processors.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── accounts/              # User Authentication App (Signup, Login, Logout)
│   ├── views.py
│   └── urls.py
├── templates/             # Django HTML Templates
│   ├── base.html
│   ├── store/
│   ├── cart/
│   └── accounts/
├── setup.py               # Automated One-Command Setup & Launcher Script
├── seed_db.py             # Database Seeding Script (Real Books & Authors)
├── db.sqlite3             # SQLite Database
├── package.json           # Project Configuration
└── README.md              # Project Documentation
```

---

## 📖 Real Sample Data Included

- **Books**: *The Great Gatsby*, *1984*, *To Kill a Mockingbird*, *Dune*, *The Hobbit*, *Clean Code*, *Designing Data-Intensive Applications*, *Atomic Habits*, *Thinking, Fast and Slow*, *Rich Dad Poor Dad*, *The Lean Startup*, etc.
- **Authors**: *F. Scott Fitzgerald*, *George Orwell*, *Harper Lee*, *Frank Herbert*, *J.R.R. Tolkien*, *Robert C. Martin*, *Martin Kleppmann*, *James Clear*, *Daniel Kahneman*, *Robert Kiyosaki*, *Eric Ries*.

---

## 📄 License

This project is open source and available under the [ISC License](LICENSE).
