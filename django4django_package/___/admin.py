from django.contrib import admin
from django.conf import settings
from django.utils.translation import gettext as _, gettext_lazy
from datetime import datetime
from django.utils.text import capfirst
from django.urls import NoReverseMatch, Resolver404, resolve, reverse
from django.apps import apps

import logging
logger = logging.getLogger("django_debug")
warning_logger = logging.getLogger("django_warning")
debug_logger = logging.getLogger("django_debug")

SITE_HEADER=getattr(settings,"SITE_HEADER","Topo")
SITE_TITLE=getattr(settings, "SITE_TITLE","Site title")
SITE_INDEX_TITLE=getattr(settings,"SITE_INDEX_TITLE","Site index title")
DEFAULT_APP_ORDER_VALUE=getattr(settings,"DEFAULT_APP_ORDER_VALUE",100)
DEFAULT_MODEL_ORDER_VALUE=getattr(settings,"DEFAULT_MODEL_ORDER_VALUE",100)


class ProjectAdminSite(admin.AdminSite):
    """
    AdminSite for admin console
    """

    def each_context(self, request):
        """
        Lets Inject some required properties to context
        """
        self.request = request
        contexto = super().each_context(request)
        contexto.update(
            {
                "admin_path": "admin",            
            }
        )
        return contexto


project_admin_site = ProjectAdminSite(name="admin-console")