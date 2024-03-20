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

With the virtual environment activated, you can now run the project. This typically involves starting the backend server and the frontend development server. Refer to specific sections below for commands related to starting these components.

Remember, keeping the project's dependencies isolated in a virtual environment helps maintain consistency across development, testing, and production environments, reducing the chance of encountering "it works on my machine" issues.

## Built With

- **Vue.js** - The web framework used.
- **Axios** - Used for making HTTP requests.
- **Vuetify** - A Material Design Framework for Vue.js (if used).

## Application Screenshots

### Main Page

![Main Page]([<link-to-main-page-image>]([https://github.com/k-aliyev/ims-fullstack/blob/master/Screenshot%202024-03-20%20171812.png)](https://raw.githubusercontent.com/k-aliyev/ims-fullstack/master/Screenshot%202024-03-20%20171812.png))

### Add Item

![Add Item](<link-to-add-item-page-image>)

### Edit Item

![Edit Item](<link-to-edit-item-page-image>)

### Delete Confirmation

![Delete Confirmation](<link-to-delete-confirmation-modal-image>)
