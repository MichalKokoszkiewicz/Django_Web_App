from django.contrib import admin


class AltAdmin(admin.AdminSite):
    site_header = "ALT-BHP"
    site_title = "ALT-BHP"
    index_title = "Panel administracyjny"
