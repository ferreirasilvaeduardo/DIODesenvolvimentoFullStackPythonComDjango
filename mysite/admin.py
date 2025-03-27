from django.contrib import admin
from django.contrib.auth.admin import GroupAdmin, UserAdmin
from django.contrib.auth.models import Group, User

from contacts.models import Contact
from polls.models import Choice, Question


class MyAdminSite(admin.AdminSite):
    site_header = (
        "Curso - Desenvolvimento Full Stack Python Com Django - Exemplo Pagina 01"
    )


admin_site = MyAdminSite()
# admin_site = MyAdminSite(name="myadmin")
admin_site.register(Choice)
admin_site.register(Question)
admin_site.register(Contact)
admin_site.register(Group, GroupAdmin)
admin_site.register(User, UserAdmin)
