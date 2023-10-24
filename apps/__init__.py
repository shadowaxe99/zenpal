
# This file is required for Python to recognize the "apps" directory as a package.

from django.apps import AppConfig

class ContactManagementConfig(AppConfig):
    name = 'contact_management'

class InteractionTrackingConfig(AppConfig):
    name = 'interaction_tracking'

class ScheduleTaskManagementConfig(AppConfig):
    name = 'schedule_task_management'

class EmailIntegrationConfig(AppConfig):
    name = 'email_integration'
