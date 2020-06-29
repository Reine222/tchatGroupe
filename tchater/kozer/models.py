from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.



class Profile(models.Model):
    """Model definition for Profile."""

    # TODO: Define fields here
    user = models.OneToOneField(User, related_name="profileUser", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="avatar")
    contact = models.CharField(max_length=250)
    lien_fb = models.URLField(max_length=200)
    lien_twt = models.URLField(max_length=200)
    lien_insta =models.URLField(max_length=200)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profileUser.save() ## prend le related_name qui le lie au model User



class Message(models.Model):
    """Model definition for Message."""

    # TODO: Define fields here
    utilisateur = models.ForeignKey(Profile, related_name="auteurMessage", on_delete=models.CASCADE)
    message = models.TextField()
    date_post = models.DateTimeField(auto_now=False, auto_now_add=True)

    status = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now=False, auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        """Meta definition for Message."""

        verbose_name = 'Message'
        verbose_name_plural = 'Messages'

    def __str__(self):
        """Unicode representation of Message."""
        return self.message



class Contact(models.Model):
    """Model definition for Contact."""

    # TODO: Define fields here
    nom = models.CharField(max_length=250)
    tel = models.CharField(max_length=250)
    image = models.ImageField(upload_to="image_contact")

    class Meta:
        """Meta definition for Contact."""

        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'

    def __str__(self):
        """Unicode representation of Contact."""
        return self.nom
