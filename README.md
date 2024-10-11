# ApnaShop-Platform

**ApnaShop** is a user-friendly e-commerce platform built with Django, offering customers and sellers a seamless online shopping experience. It includes features such as product browsing, secure payments, easy account management, and more.

---

## Features

- **User Authentication**:
  - Sign up, log in, log out with secure password storage and session management.

- **Product Listings**:
  - Browse products by categories with detailed descriptions, prices, and availability.

- **Shopping Cart**:
  - Add, remove, and update items in the cart. It automatically updates total cost and quantity.

- **CSRF Protection**:
  - Built-in security using Django’s CSRF protection for secure user interactions.

- **Payments Integration**:
  - Secure payments via gateways supporting methods like credit/debit cards, UPI, and net banking.

- **Order Management**:
  - Track order history and check current order status from user profiles.

- **Admin Dashboard**:
  - Manage products, inventory, orders, and customers via a powerful admin interface.

---

## Getting Started

### 1. Installation

Clone the repository:

```bash
git clone https://github.com/Hariomkabra/ApnaShop-Platform.git
cd apnashop
```

### 2. Environment Variables

Set up the required environment variables:

```
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=your_database_url
PAYMENT_GATEWAY_API_KEY=your_payment_gateway_key
```

### 3. Database Setup

Run the migrations to set up the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 4. Run the Server

Start the development server:

```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`.

---

## Key Concepts

- **CSRF Tokens**: Protects form submissions from unauthorized access using unique CSRF tokens.
  
- **User Authentication**: Users register with an email and password. Sessions are managed securely using Django's authentication system.

- **Payments**: Orders are processed securely through integrated payment gateways with instant confirmation.

- **Cart Management**: Items can be added, updated, and removed from the cart. Cart data is synced with the server for logged-in users.

- **Product Management**: Admins and sellers can manage products, including details like price, description, and availability.

- **Order History**: Users can view past orders, track current orders, and check order statuses.

---

## How to Use

1. **Add Products to Cart**:
   Browse and click "Add to Cart" on the items you want to purchase. Review the cart using the cart icon.
   
2. **Checkout & Payment**:
   Proceed to checkout, complete the payment via the integrated gateway, and receive an order confirmation.
   
3. **Login/Signup**:
   To purchase, users must log in. If you don't have an account, sign up using your email and password.
   
4. **Manage Your Account**:
   After logging in, manage your personal information, view past orders, and update your password.

---

## Tech Stack

- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite/PostgreSQL
- **Payment Gateway**: Razorpay, Stripe, Paytm

---

## Local Development

To run the project locally, use:

```bash
python manage.py runserver
```

Visit the application at `http://127.0.0.1:8000/`.

---

## License

ApnaShop is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## Contributions

We welcome contributions! Feel free to fork the repository, make improvements, and create pull requests.
