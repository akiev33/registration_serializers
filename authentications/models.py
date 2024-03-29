import uuid
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):

    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)

    send_mail(
        # title:
        "Сброс пароля {title}".format(title=""),
        # message:
        email_plaintext_message,
        # from:
        "noreply@somehost.local",

        [reset_password_token.user.email]
    )


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=False,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
        ordering = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email



class User(AbstractEmailUser):

    USER_TYPE_CHOICES = (
        ('user', 'User'),
    )
    GENDER_TYPE_CHOICES = (
        ('man', 'Man'),
        ('woman', 'Woman')
    )
    user_type = models.CharField(
        choices=USER_TYPE_CHOICES,
        max_length=255, blank=True
    )

    gender_type = models.CharField(
        choices=GENDER_TYPE_CHOICES,
        max_length=255, blank=True
    )

    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField('last name', max_length=255, blank=True)
    age = models.PositiveIntegerField()
    activation_code = models.CharField(max_length=36, blank=True)

    def get_full_name(self):
        return self.last_name

    def get_short_name(self):
        return self.last_name

    def create_activation_code(self):
        self.activation_code = str(uuid.uuid4())

    def __str__(self):
        return '{name} < {email}'.format(
            name=self.last_name,
            email=self.email
        )


