from django.contrib.auth.models import AbstractUser
from django.core.validators import FileExtensionValidator, RegexValidator
from django.db import models
from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


# Create your models here.:

class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(_("phone number"), max_length=20, validators=[RegexValidator(r'^\+?1?\d{9,13}$')], blank=True, null=True)
    # photo = models.ImageField(_("photo"), upload_to='user_photos/', null=True, blank=True,
    #                           validators=[FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])
    username = models.CharField(
        _("username"),
        max_length=150,
        error_messages={
            "unique": _("A user with that username already exists."),
        },
        null=True,
        blank=True
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    USERNAME_FIELD = "email"
    objects = UserManager()

    REQUIRED_FIELDS = []

    # trainings_plans = models.ForeignKey(TrainingPlans, on_delete=models.CASCADE, related_name="owner")
    # trainings_units = model.ForeignKey(TrainingUnits, on_delete=models.CASCADE, related_name="owner")
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


