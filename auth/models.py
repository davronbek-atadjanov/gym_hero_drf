from django.db import models
from django.utils.translation import gettext_lazy as _

from auth.utils import check_otp_code


class VerificationOtp(models.Model):
    class VerificationType(models.TextChoices):
        REGISTER = "register", _("register")
        RESET_PASSWORD = "reset_password", _("reset_password")
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name="verification_otp")
    code = models.IntegerField(_('verification code'), validators=[check_otp_code])
    type = models.CharField(_('verification type'), max_length=20, choices=VerificationType.choices)
    expires_in = models.DateTimeField(_('expires in'))
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.email} | code: {self.code}"

    class Meta:
        verbose_name = _('verification otp')
        verbose_name_plural = _('verification otps')
        ordering = ["-expires_in"]
    
