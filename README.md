# Recipe App (Django Web Application)

## Project Overview

The **Recipe App** is a dynamic, multi-user web application built using the Django framework. It allows users to search for and browse recipes while also providing a robust admin panel for data management. This project demonstrates proficiency in full-stack web development with Python and Django, emphasizing efficient database interactions, data visualization, testing and user-friendly design.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [User Stories](#user-stories)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

### Core Features

- **User Authentication:**
  - Users can log in and log out securely.
  
- **Recipe Management:**
  - The recipe model includes attributes for name, description, prep time, cooking time, difficulty, ingredients, and pictures.
  
- **Search Functionality:**
  - Filter recipe preview cards based on name, ingredients, or difficulty.

- **Recipe Details:**
  - Display extended details for selected recipes.

- **Admin Panel:**
  - Manage users and recipes with CRUD capabilities, analyze site data.

### Additional Features

- Analytics Charts:
  - Visualize data like ingredient frequency, recipe difficulty percentage, and total time per recipe.
- Data Handling:
  - Leverage a PostgreSQL database for production.
- Error Handling:
  - Provide user-friendly error messages for invalid inputs.

## User Stories

- **As a user**, I want to log in and view my recipes so that I can keep track of my personal collection.
- **As a user**, I want to filter recipes based on specific criteria.
- **As a user**, I want to analyze recipe trends and view charted recipe data.
- **As an admin**, I want to easily modify recipes and user information from the admin dashboard.

## Setup and Installation

Follow these steps to set up the Recipe App locally:

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/recipe-app-django.git
   ```

2. **Navigate to the project directory:**
   ```sh
   cd src
   ```

3. **Create and activate a virtual environment:**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows: env\Scripts\activate
   ```

4. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

5. **Create a `.env` File:**
   
   In the project's root directory (src), create a `.env` file.
   Add the following content to the .env file:
   ```sh
   SECRET_KEY = 'your-secret-key'
   ```
   Replace `'your-secret-key'` with a secure key.

7. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

8. **Create a superuser for admin access:**
   ```sh
   python manage.py createsuperuser
   ```

9. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

   Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

1. Register or log in to your account.
2. Create and manage your recipes via the admin dashboard.
3. Search for recipes based on ingredients or browse all available recipes.
4. Visualize analytics by generating charts for insights into recipe trends.
5. View extended details of selected recipes.

## Deployment

The application will be deployed on Heroku.

## Contributing

Contributions are welcome!

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
