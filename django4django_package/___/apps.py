from django.contrib.admin.apps import AdminConfig
from django.utils.translation import gettext_lazy as _


class AdminSiteConfig(AdminConfig):
    verbose_name = _("Test admin site")