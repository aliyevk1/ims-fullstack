# Inventory Management System

Inventory Management System is a web application designed to manage inventory. It offers features for adding, viewing, editing, and deleting items. This document provides guidance on setting up and running the application locally and introduces its main functionalities.

## Application Features

- **View Items**: Allows users to see all items stored in the database.
- **Add New Items**: Users can add new items through a user-friendly form.
- **Edit Items**: Existing items can be modified by the users.
- **Delete Items**: Enables item deletion with a confirmation step to prevent accidental deletions.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Before you start, ensure you have the following installed:
- Node.js
- Vue CLI
- A modern web browser
- pipenv

## Setting Up the Project Environment

This project uses `pipenv` for managing its environment and dependencies, ensuring consistent setups across different machines and isolating the project dependencies from global Python packages.

> **Note**
> You can avoid using pipenv by simply removing `Pipfile` and `Pipfile.lock` and installing all dependencies globally.

### Installation

After cloning the repository to your local machine:

1. **Navigate to the Project Directory**: Change into the project directory where the `Pipfile` and `Pipfile.lock` are located.

2. **Install Dependencies**: Use `pipenv` to install the project dependencies. This step will create a new virtual environment specific to this project and install all the necessary packages as defined in the `Pipfile.lock`, ensuring you have the exact versions of each package.

### Activating the Virtual Environment

Once the dependencies are installed, you'll need to activate the virtual environment managed by `pipenv`. This ensures that the correct versions of the packages are used when running the project or any related commands.

### Running the Project

## Running the Project

This project is divided into two main parts: the Django backend and the Vue.js frontend. Follow the steps below to get both parts up and running on your local machine.

### Running the Django Backend

1. **Activate the Virtual Environment**: Before running the Django project, make sure you've activated the virtual environment created by `pipenv`. This ensures that the correct versions of dependencies are used.

2. **Navigate to the Backend Directory**: Change your directory to where the Django project is located.

3. **Apply Migrations**: Ensure your database is up to date with the latest migrations.

    ```
    python manage.py migrate
    ```

4. **Start the Django Development Server**: Use the following command to start the server:

    ```
    python manage.py runserver
    ```

    By default, the server will start on `http://localhost:8000`. You can access the Django admin panel or API endpoints from this address.

### Running the Vue.js Frontend

1. **Navigate to the Frontend Directory**: Change your directory to where the Vue.js project is located.

2. **Install Dependencies**: If this is your first time running the project, or if new dependencies have been added, you'll need to install them using `npm` or `yarn`.

    ```
    npm install
    ```

    or

    ```
    yarn install
    ```

3. **Start the Vue Development Server**: Use the following command to compile and hot-reload for development:

    ```
    npm run serve
    ```

    or

    ```
    yarn serve
    ```

    The Vue development server typically starts on `http://localhost:8080`. Open this URL in your browser to view and interact with your Vue.js application.

### Note on API Connectivity

Ensure that the Vue.js frontend is correctly configured to communicate with the Django backend API. This often involves setting the correct base URL for API requests in your Vue.js application's environment variables or configuration files.


## Built With

- **Vue.js** - The web framework used.
- **Axios** - Used for making HTTP requests.
- **Vuetify** - A Material Design Framework for Vue.js (if used).
## Application Screenshots

### Main Page - Table View
![Main Page - Table View](https://raw.githubusercontent.com/k-aliyev/ims-fullstack/master/Screenshot%202024-03-20%20171812.png)

### Delete Modal
![Delete Modal](https://raw.githubusercontent.com/k-aliyev/ims-fullstack/master/Screenshot%202024-03-20%20171827.png)

### Edit Item
![Edit Item](https://raw.githubusercontent.com/k-aliyev/ims-fullstack/master/Screenshot%202024-03-20%20171841.png)

### Add Item - Empty Form
![Add Item - Empty Form](https://raw.githubusercontent.com/k-aliyev/ims-fullstack/master/Screenshot%202024-03-20%20171933.png)

### Add Item - Filled with Example
![Add Item - Filled with Example](https://raw.githubusercontent.com/k-aliyev/ims-fullstack/master/Screenshot%202024-03-20%20171951.png)

### Updated Table After Example Add
![Updated Table After Example Add](https://raw.githubusercontent.com/k-aliyev/ims-fullstack/master/Screenshot%202024-03-20%20172002.png)

