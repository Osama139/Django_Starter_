from django.db import models
from django.contrib.auth.models import User
from django.templatetags.static import static


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='avatars/', null=True, blank=True)
    displayname = models.CharField(max_length=20, null=True, blank=True)
    info = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.user)

    @property
    def name(self):
        """Return the display name if available, otherwise return the username."""
        return self.displayname if self.displayname else self.user.username

    @property
    def avatar(self):
        """Return the URL of the avatar image, or a default if the image is not available."""
        try:
            avatar = self.image.url
        except:
            avatar = static('images/avatar.svg')
        return avatar
