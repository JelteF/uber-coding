"""Module that implements sending of emails.

This is done redundantly with multiple email providers.
"""

import sendgrid
from mailgun2 import Mailgun
from mandrill import Mandrill
from ses_mailer import Mail as SesMailer

from app import app, config

_mailers = {
    'sendgrid': sendgrid.SendGridClient(config['SENDGRID_API_KEY']),
    'mailgun': Mailgun(config['MAILGUN_FROM_DOMAIN'],
                       config['MAILGUN_PRIVATE_KEY'],
                       config['MAILGUN_PUBLIC_KEY']),
    'mandrill': Mandrill(config['MANDRILL_API_KEY']),
    'ses': SesMailer().init_app(app),
}


class RedundantMail():
    """A simple class to send email using multiple providers."""

    def __init__(self, to_email, subject, body, from_email=None):
        self.to_email = to_email
        self.subject = subject
        self.body = body

        if from_email is None:
            from_email = config['DEFAULT_FROM_EMAIL']
        self.from_email = from_email

    def send(self):
        """Try to send the email all available providers."""

        sub_errors = []

        for provider in config['PROVIDER_ORDER']:
            try:
                if provider == 'sendgrid':
                    self.sendgrid()
                elif provider == 'mailgun':
                    self.mailgun()
                elif provider == 'mandrill':
                    self.mandrill()
                elif provider == 'ses':
                    self.ses()
            except Exception as e:
                sub_errors.append(e)
                continue
            return provider

        else:
            raise RuntimeError('All providers failed, something serious is '
                               'probably wrong.', sub_errors)

    def mailgun(self):
        """Send with Mailgun."""
        resp = _mailers['mailgun'].send_message(self.from_email,
                                                [self.to_email],
                                                Subject=self.subject,
                                                Text=self.body)

        if not resp.ok:
            raise RuntimeError('Mailer returned an error.', resp)

    def sendgrid(self):
        """Send with Sendgrid."""
        message = sendgrid.Mail(to=self.to_email,
                                subject=self.subject,
                                text=self.body,
                                from_email=self.from_email)

        status, error_msg = _mailers['sendgrid'].send(message)

        if status != 200:
            raise RuntimeError('Mailer returned an error.', status, error_msg)

    def mandrill(self):
        """Send with Mandrill."""
        ...

    def ses(self):
        """Send with Amazon SES."""
        ...
