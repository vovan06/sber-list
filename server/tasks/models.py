import uuid

from django.db import models
from django.urls import reverse_lazy
from authsystem.models import User

class TaskStatus(models.Model):
    title = models.CharField(max_length=64)
    discription = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        verbose_name = ("Task Status")
        verbose_name_plural = ("Task Statuses")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("status_detail", kwargs={"pk": self.pk})

class SubTask(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=64)
    file = models.FileField(upload_to='tasks/sub/', blank=True, null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, related_name='sub_status')
    participants = models.ManyToManyField(User, blank=True, related_name='sub_participants')
    deadline = models.DateField(blank=True, null=True)


    class Meta:
        verbose_name = ("sub task")
        verbose_name_plural = ("Sub tasks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("sub_task_detail", kwargs={"pk": self.id})


class MainTask(models.Model):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=64)
    discription = models.CharField(max_length=256, blank=True, null=True)
    file = models.FileField(upload_to='tasks/main/', blank=True, null=True)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT, related_name='main_status')
    sub_task = models.ManyToManyField(SubTask, blank=True, related_name='sub_tasks')
    participants = models.ManyToManyField(User, blank=True, related_name='main_participants')
    deadline = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = ("Main task")
        verbose_name_plural = ("Main tasks")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy("task_detail", kwargs={"pk": self.id})