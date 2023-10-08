from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from post.models import Post

@receiver(post_save, sender=Post)
def send_post_creation_notification(sender, instance, created, **kwargs):
    print("signal triggered...")
    if created:
        print("post created...")
        subject = 'New Post Created'
        message = f'Hello {instance.author.username},\n\nYour new post "{instance.title}" has been created.'
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [instance.author.email]
        print(subject, message, from_email, recipient_list)
        send_mail(subject, message, from_email, recipient_list)
