
# CRM Application

## Overview
This is a Django-based Customer Relationship Management (CRM) application. It includes various functionalities like contact management, interaction tracking, and schedule and task management.

## Functionalities
- **Contact Management**: Allows for CRUD operations on contacts. [Read More](./apps/contact_management/README.md)
- **Interaction Tracking**: Enables tracking of interactions with contacts. [Read More](./apps/interaction_tracking/README.md)
- **Schedule and Task Management**: Helps in managing tasks and schedules. [Read More](./apps/schedule_task_management/README.md)

## File Tree
```
CRM_App 3/
├── apps/
│   ├── contact_management/
│   │   ├── README.md
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── interaction_tracking/
│   │   ├── README.md
│   │   ├── models.py
│   │   ├── urls.py
│   │   └── views.py
│   └── schedule_task_management/
│       ├── README.md
│       ├── models.py
│       ├── urls.py
│       └── views.py
├── CRM_App/
│   ├── settings.py
│   ├── urls.py
│   └── manage.py
└── README.md
```

## Getting Started
To get the application running, you'll need to have Django installed. Navigate to the `CRM_App` directory and run the following command:
```
python manage.py runserver
```
This will start the development server, and the application will be accessible at `http://localhost:8000/`.
