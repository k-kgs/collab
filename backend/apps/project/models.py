from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.user.models import User
import uuid

class Project(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=255,
        null=False,
        blank=False,
        db_index=True
    )
    description = models.CharField(
        max_length=455,
        null=True,
        blank=True,
        default="-",
        db_index=True
    )
    start_date = models.DateField(_("Start Date"), null=False)
    estimated_delivery_date = models.DateField(_("End Date"), null=False)
    is_active = models.BooleanField(
        _("Active"),
        default=True
    )
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)



class ProjectUserMapping(models.Model):
    project = models.ForeignKey(
        Project,
        related_name="Project_Mapping",
        verbose_name=_("project mapping"),
        on_delete=models.CASCADE,
        db_index=True
    )
    user = models.ForeignKey(
        User,
        related_name="User_Mapping",
        verbose_name=_("user mapping"),
        db_index=True,
        on_delete=models.CASCADE
    )
    is_owner = models.BooleanField(default=False, null=False, blank=False)
    is_active = models.BooleanField(
        _("Active"),
        default=True
    )
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)