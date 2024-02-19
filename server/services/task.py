from server.celery import app
from django.core.mail import send_mail

from server.settings import DEFAULT_FROM_EMAIL
from server.settings import ALLOWED_HOSTS

# @app.task()
def _archive_project(project, instance=None):
        project.status = instance
        for i in project.tasks.all():
            i.status = instance
            for j in i.sub_task.all():
                j.status = instance
                j.save()
            i.save()
        project.save()

# @app.task()
def sending_mail(email, subject, text):    
        send_mail(
        subject,
        text,
        DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=True,
    )