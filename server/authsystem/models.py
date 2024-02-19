import jwt
import uuid
from django.db import models
from django.conf import settings
from django.urls import reverse_lazy
from datetime import datetime, timedelta
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager,
)
from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Password Reset for {title}".format(title="Some website title"),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",
        # to:
        [reset_password_token.user.email]
    )
def reset_request(request):
    data = request.data
    email = data['email']
    user = CustomUser.objects.get(email=email)
    if CustomUser.objects.filter(email=email).exists():
        # send email with otp
        send_mail(
        'Subject here',
        f'Here is the message with {user.otp}.',
        'from@example.com',
        [user.email],
        fail_silently=False,
        )
        message = {
            'detail': 'Success Message'}
        return Response(message, status=status.HTTP_200_OK)
    else:
        message = {
            'detail': 'Some Error Message'}
        return Response(message, status=status.HTTP_400_BAD_REQUEST)

class UserManager(BaseUserManager):
    def create_user(self, name, surname, patronymic, email, password, **kwargs):
        if email is None:
            raise TypeError('Users must have an email address.')
        
        if password is None:
            raise TypeError('Users must have an email address.')

        user = self.model(email=self.normalize_email(email))
        user.name = name
        user.surname = surname
        user.patronymic = patronymic
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, password, **kwargs):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.private_access = True
        user.save()

        return user


class User(AbstractBaseUser):
    id = models.UUIDField(
        primary_key=True,
        db_index=True,
        default=uuid.uuid4,
        editable=False
    )
    
    email = models.EmailField(max_length=256, unique=True)
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    patronymic = models.CharField(max_length=64, null=True, blank=True)
    telegram_user_id = models.CharField(max_length=32, null=True, blank=True)
    avatar = models.ImageField(upload_to='user/avatar/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False) 
    is_staff = models.BooleanField(default=False)

    # Auth settings
    USERNAME_FIELD = 'email'

    objects = UserManager()

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_absolute_url(self,):
        return reverse_lazy('moder_user_detail', kwargs={'id': self.id})

    class Meta:
        indexes = [
            models.Index(fields=['id'], name='id_index'),
        ]