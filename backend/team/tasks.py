from django.core.mail import send_mail


def send_invitation_email(invitation):
    message = f"""Hi {invitation.email},
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
        recipient_list=[invitation.email],
    )
