from django.contrib.admin.apps import AdminConfig


class AltAdminConfig(AdminConfig):
    default_site = 'altbhp_admin.admin.AltAdmin'
