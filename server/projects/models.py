import uuid
from django.db import models
from django.urls import reverse_lazy

from authsystem.models import User
from tasks.models import TaskStatus, MainTask

class Project(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=64)
    discription = models.CharField(max_length=256, blank=True, null=True)
    file = models.FileField(upload_to='projects/main/', blank=True, null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, related_name='project_participants')
    tasks = models.ManyToManyField(MainTask, blank=True, related_name='project_tasks')
    participants = models.ManyToManyField(User, blank=True, related_name='project_participants')
    deadline = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = ("Main task")
        verbose_name_plural = ("Main tasks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("project_detail", kwargs={"pk": self.id})