
# Schedule and Task Management Functionality

## Overview
The schedule and task management functionality is designed to help users manage their tasks and schedules. It offers CRUD (Create, Read, Update, Delete) operations on tasks, each of which is associated with a user and has attributes like title, description, and completion status.

## Key Files
### `models.py`
Defines two main classes:
- `Task`: Includes fields like `user`, `title`, `description`, `complete`, and `created`.
- `Schedule`: Although not fully visible, this model appears to be linked to the `User` and `Task` models.

### `urls.py`
Maps URL paths to specific views/functions. The following routes are defined:
- `index`: List all tasks
- `create_task`: Create a new task
- `update_task`: Update an existing task
- `delete_task`: Delete a task

### `views.py`
Implements the logic for task-related functionalities. For example:
- The `index` function fetches all tasks from the database and renders them in an HTML template.
- The `create_task` function creates a new task using POST data.

## Features
- List all tasks associated with a user
- Add a new task
- Update an existing task
- Delete a task
