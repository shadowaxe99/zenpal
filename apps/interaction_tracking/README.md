
# Interaction Tracking Functionality

## Overview
The interaction tracking functionality allows users to keep a record of their interactions with contacts. It provides CRUD (Create, Read, Update, Delete) operations on interaction records. Each interaction is linked to a contact and has attributes like date and notes.

## Key Files
### `models.py`
Defines the `Interaction` model which has the following fields:
- `contact`: A foreign key linked to the `Contact` model from the `contact_management` app.
- `date`: A timestamp for when the interaction occurred.
- `notes`: A text field to store any relevant notes.

### `urls.py`
Maps URL paths to specific views and functions in the application. The following routes are defined:
- `index`: List all interactions
- `add_interaction`: Add a new interaction
- `edit_interaction`: Edit an existing interaction
- `delete_interaction`: Delete an interaction

### `views.py`
Implements the logic for interaction-related functionalities. For example:
- The `index` function fetches all interactions from the database and renders them in an HTML template.
- The `create` function adds a new interaction record if the HTTP request method is POST.

## Features
- List all interactions linked to contacts
- Add a new interaction
- Edit an existing interaction
- Delete an interaction

## Integration with `contact_management`
The interaction records are closely tied to the contacts stored in the `contact_management` functionality. The `contact` field in the `Interaction` model is a foreign key that links to the `Contact` model, ensuring that every interaction is associated with a specific contact.
