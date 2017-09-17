from time import timezone

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Override base user
    This is the class which describes the standard user
    """
    username = models.CharField(max_length=32, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False)
    is_active = models.BooleanField(_('is active'), default=True)
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    # Below isn't required fields
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        db_table = 'auth_user'

    def get_short_name(self):
        if self.first_name or self.last_name:
            return ' '.join((self.first_name, self.last_name))
        return self.email


class TypeTest(models.Model):
    """
    Model for different type of tests.
    For example: Python level 1, Python level 2, Java level 1 and etc.
    """
    type_test = models.CharField(max_length=200)

    def __str__(self):
        return self.type_test.capitalize()


class Question(models.Model):
    """Model for questions."""
    question_text = models.CharField(max_length=400)
    type_test = models.ForeignKey(TypeTest, on_delete=models.CASCADE)  # the communication is many-to-one

    def __str__(self):
        return self.question_text


class Option(models.Model):
    """Model for test options."""
    option = models.CharField(max_length=200)
    truth = models.BooleanField()  # can be False if option is not right or True if is truth
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # the communication is many-to-one

    def __str__(self):
        return 'Option is {} - {}'.format(self.option, self.truth)
