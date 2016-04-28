"""Default configuration of the webserver."""


class DefaultConfig:
    """Default configuration."""

    DEBUG = True
    SECRET_KEY = 'SOMETHING_SUPER_SECRET'
    DEFAULT_FROM_EMAIL = 'from@example.com'

    PROVIDER_ORDER = ['sendgrid', 'mailgun', 'mandrill', 'ses']

    # Configs for different email providers
    SENDGRID_API_KEY = ''

    MAILGUN_FROM_DOMAIN = 'mg.example.com'
    MAILGUN_PRIVATE_KEY = ''
    MAILGUN_PUBLIC_KEY = ''

    MANDRILL_API_KEY = ''

    SES_AWS_ACCESS_KEY = ''
    SES_AWS_SECRET_KEY = ''
    SES_SENDER = DEFAULT_FROM_EMAIL
