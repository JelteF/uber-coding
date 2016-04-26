"""Module that implements sending of emails.

This is done redundantly with multiple email providers.
"""

import sendgrid
from mailgun2 import Mailgun
from mandrill import Mandrill
from ses_mailer import Mail as SesMailer

from app import app, config

mailers = {
    'sendgrid': sendgrid.SendGridClient(config['SENDGRID_API_KEY']),
    'mailgun': Mailgun(config['MAILGUN_FROM_DOMAIN'],
                       config['MAILGUN_PRIVATE_KEY'],
                       config['MAILGUN_PUBLIC_KEY']),
    'mandrill': Mandrill(config['MANDRILL_API_KEY']),
    'ses': SesMailer().init_app(app),
}


def send_mail(to_email, subject, body, from_email=None):
    """Simple interface to send an actual email."""

    if from_email is None:
        from_email = config['DEFAULT_FROM_EMAIL']

    for provider in config['PROVIDER_ORDER']:
        mailer = mailers[provider]

        if provider == 'sendgrid':
            message = sendgrid.Mail(to=to_email, subject=subject, text=body,
                                    from_email=from_email)

            try:
                status, _ = mailer.send(message)
            except:
                continue

            if status == 200:
                break

        elif provider == 'mailgun':

            try:
                resp = mailer.send_message(from_email, [to_email],
                                           subject=subject,
                                           text=body)
            except:
                continue

            if resp.ok:
                break

        elif provider == 'mandrill':
            ...

        elif provider == 'ses':
            ...
    else:
        raise RuntimeError('All providers failed, something else is probably '
                           'wrong')
    return provider
