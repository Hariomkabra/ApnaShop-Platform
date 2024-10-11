# ApnaShop-Platform
ApnaShop is a user-friendly e-commerce platform built with Django, designed to provide customers with a seamless online shopping experience. It offers features such as product browsing, like shopping and easy account management. 

# ApnaShop

**ApnaShop** is a comprehensive e-commerce platform designed for efficient online shopping, offering a user-friendly experience for both buyers and sellers. This platform is built using Django and provides various functionalities like product listings, secure payments, user authentication, and a cart system.

---

## Features

- **User Authentication**: 
  - Users can easily sign up, log in, and log out. The platform also supports user sessions and secure password storage.
  
- **Product Listings**: 
  - ApnaShop allows users to browse through product categories and view detailed descriptions, prices, and availability for each item.
  
- **Shopping Cart**:
  - A fully functional cart that allows users to add and remove items. The cart dynamically updates the total cost and item quantity.

- **CSRF Protection**: 
  - The platform implements Django's built-in Cross-Site Request Forgery (CSRF) protection to ensure secure user interactions, especially during sensitive actions like form submissions and payments.

- **Payments Integration**: 
  - Secure payment gateways allow customers to complete their purchases seamlessly. The platform handles various payment methods like credit/debit cards, net banking, and UPI.

- **Order Management**: 
  - Users can track their order history and view the status of their current orders directly from their profile.

- **Admin Dashboard**:
  - A powerful admin interface for sellers and admins to manage products, inventory, orders, and customers.

---

## Getting Started

### 1. Installation

To set up the project locally, clone the repository:

```bash
git clone https://github.com/Hariomkabra/ApnaShop-Platform.git

Navigate to the project directory and install dependencies:
cd apnashop

### 2. Environment Variables
SECRET_KEY=your_django_secret_key
DEBUG=True
DATABASE_URL=your_database_url
PAYMENT_GATEWAY_API_KEY=your_payment_gateway_key

### 3. Migrations
Make sure to run the migrations to set up the database:
python manage.py makemigrations
python manage.py migrate


Key Concepts:

CSRF Tokens:
The platform uses Django's default CSRF protection to ensure that forms and sensitive actions are protected from unauthorized access or attacks. Every form submission includes a unique CSRF token.
User Authentication
Users can register using their email and password. Upon successful registration or login, user sessions are created to manage authentication. The login and logout functionalities are securely handled using Django's authentication system.

Payments:
Secure payments are managed using integrated payment gateways. When a user completes an order, the payment is processed through the gateway, and the user receives a confirmation.

Cart Management:
Users can add products to their cart, increase or decrease the quantity, and remove products. The cart is saved in local storage and synced with the server when the user is logged in.

Login & Logout:
ApnaShop provides a secure and easy way to log in and out of the platform. Login and logout endpoints ensure the user's session is properly managed, and secure redirects are implemented.

Product Management:
Sellers and admins can add, update, or delete products from the platform through the admin interface. Each product includes details like price, description, and stock availability.

Order History:
Users can view their past orders, check order statuses, and review their purchase history



How to Use:
1. Adding Products to Cart
Browse through the product listings and click on "Add to Cart" for the items you'd like to purchase. You can view the cart summary in the cart icon at the top of the page.
2. Checkout & Payments
Once you're ready, click the checkout button. The system will redirect you to the payment gateway where you can complete the purchase. Once the payment is successful, you'll be redirected to an order confirmation page.
3. Login/Signup
To make purchases, users need to be logged in. If you don't have an account, you can sign up using your email and password.
4. Managing Your Account
After logging in, you can manage your account, update personal details, view past orders, and change your password.

Tech Stack:
Django: Backend framework
HTML/CSS/JavaScript: Frontend
SQLite/PostgreSQL: Database
Bootstrap: Frontend framework
Payment Gateway: Integrated payment solutions (e.g., Razorpay, Stripe,Paytm)![Apnashop01](https://github.com/user-attachments/assets/428b6950-3416-4bb5-aa0e-4c3595a02b82)


Local Development:
To run the project locally:
Use Command "python manage.py runserver"
Visit the application at  "  http://127.0.0.1:8000 "

ApnaShop is licensed under the MIT License.

Contributions
We welcome contributions! Feel free to fork this repository and create pull requests to enhance the platform.
