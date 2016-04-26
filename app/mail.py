"""Module that implements sending of emails.

This is done redundantly with multiple email providers.
"""

from sendgrid import SendGridClient
from mailgun2 import Mailgun
from mandrill import Mandrill
from ses_mailer import Mail as SesMailer

from app import app, config

mailers = {
    'sendgrid': SendGridClient(config['SENDGRID_API_KEY']),
    'mailgun': Mailgun(config['FROM_DOMAIN'],
                       config['MAILGUN_PRIVATE_KEY'],
                       config['MAILGUN_PUBLIC_KEY']),
    'mandrill': Mandrill(config['MANDRILL_API_KEY']),
    'ses': SesMailer().init_app(app),
}


def send_mail(to_email, subject, body, from_email=None):
    """Simple interface to send an actual email."""

    if from_email is None:
        from_email = config['DEFAULT_FROM_EMAIL']

    print(to_email, subject, body, from_email)
