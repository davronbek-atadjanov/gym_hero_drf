from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


# Create your models here.:

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_("email address"), unique=True)
    phone_number = models.CharField(
        _("phone number"),
        max_length=20,
        validators=[RegexValidator(r'^\+?1?\d{9,13}$')],
        blank=True,
        null=True
    )
    is_active = models.BooleanField(
        _("active"),
        default=False,  # Yangi foydalanuvchi har doim faol emas
        help_text=_("Designates whether this user should be treated as active."),
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["phone_number"]
    objects = UserManager()

    # trainings_plans = models.ForeignKey(TrainingPlans, on_delete=models.CASCADE, related_name="owner")
    # trainings_units = model.ForeignKey(TrainingUnits, on_delete=models.CASCADE, related_name="owner")
    def __str__(self):
        return self.email

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")


