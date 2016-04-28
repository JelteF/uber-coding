"""Routes of the web application."""

from flask import render_template, url_for, redirect, request

from app.mail import RedundantMail
from app import app


@app.route('/')
def home():
    """Route for the homepage."""

    return render_template('home.jade')


@app.route('/mail', methods=['POST'])
def send_email():
    """Route to send actual email."""

    used_form_vals = {k: request.form[k] for k in
                      ['to_email', 'subject', 'body']}

    RedundantMail(**used_form_vals).send()

    return redirect(url_for('home'))
