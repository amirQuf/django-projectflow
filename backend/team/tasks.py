from django.core.mail import send_mail
from .models.invitation import Invitation


from celery import shared_task
from django.utils import timezone


@shared_task
def send_invitation_email(invitation):
    message = f"""Hi {invitation.user.username},
You have been invited to join the team "{invitation.team.name}"," 
Click the link below to accept the invitation and join the team:
{invitation.invite_link()}
This invitation will expire on {invitation.expires_at}.
If you did not expect this invitation, you can safely ignore this email.
Welcome aboard!
— The {invitation.team.name} Team
"""

    send_mail(
        subject="You're invited!",
        message=message,
        from_email="no-reply@yourapp.com",
        recipient_list=[invitation.user.email],
    )


@shared_task
def set_expired_status(self):
    """
    find invitations that is expires and set their status
    """
    try:
        now = timezone.now()
        expired = Invitation.objects.filter(
            expires_at__lt=now, status__in=["pending", "sent"]
        )
        count = expired.count()
        expired.update(status="expired")
        print(f"{count} invitations marked expired.")
    except Exception as e:
        raise self.retry(exc=e)
