
# Contact Management Functionality

## Overview
The contact management functionality allows for CRUD (Create, Read, Update, Delete) operations on contacts. Each contact has a set of attributes like name, email, phone number, and address.

## Key Files
- `models.py`: Defines the `Contact` model with fields like `first_name`, `last_name`, `email`, `phone`, and `address`.
- `urls.py`: Maps URL paths to specific views/functions for displaying, adding, editing, and deleting contacts.
- `views.py`: Implements the logic for the functionalities, including fetching all contacts, displaying a single contact's details, and adding a new contact.

## Features
- List all contacts
- Add a new contact
- Edit an existing contact
- Delete a contact
