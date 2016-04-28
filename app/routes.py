"""Routes of the web application."""

from flask import render_template, request, flash

from app.mail import RedundantMail
from app import app

import logging


@app.route('/')
def home():
    """Route for the homepage."""

    return render_template('home.jade')


@app.route('/', methods=['POST'])
def send_mail():
    """Route to send actual email."""

    used_form_vals = {k: request.form[k] for k in
                      ['to_email', 'subject', 'body']}

    try:
        provider = RedundantMail(**used_form_vals).send()
    except RuntimeError as e:
        flash(str(e), 'danger')
        logging.exception(str(e))
        return_code = 502
    else:
        flash("Email was successfully sent using " + provider.capitalize(),
              'success')
        return_code = 200

    return home(), return_code
