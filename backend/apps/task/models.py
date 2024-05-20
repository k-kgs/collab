from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.project.models import Project
from apps.user.models import User
import uuid

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(
        Project,
        related_name="Task_Project_Mapping",
        verbose_name=_("project mapping"),
        on_delete=models.CASCADE,
        db_index=True
    )
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
    class Status(models.TextChoices):
        TODO = "TODO", _("TO DO")
        INPROGRESS = "INPROGRESS", _("In Progress")
        REVIEW = "REVIEW", _("Review")
        DONE = "DONE", _("Done")
    

    status = models.CharField(
        _("Status"),
        max_length=25,
        blank=True,
        null=True,
        choices=Status.choices
    )
    is_active = models.BooleanField(
        _("Active"),
        default=True
    )
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)



class TaskUserMapping(models.Model):
    task = models.ForeignKey(
        Task,
        related_name="Task_User_Project_Mapping",
        verbose_name=_("project mapping"),
        on_delete=models.CASCADE,
        db_index=True
    )
    user = models.ForeignKey(
        User,
        related_name="Task_User_Mapping",
        verbose_name=_("user mapping"),
        db_index=True,
        on_delete=models.CASCADE
    )
    is_owner = models.BooleanField(default=False, null=False, blank=False)
    date_created = models.DateTimeField(_("Date Created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("Date Updated"), auto_now=True)