# Uber Email service

## Problem
Sending email reliably can be very important.
This project abstracts the sending of four email providers, Sendgrid, Mailgun,
Mandrill and Amazon SES.
By providing some basic information in a form an email can be sent reliably
using this service.

## Focus
This solution focusses on the back-end. A basic front-end is provided but
nothing fancy.

## Architectural choices
This code is written in Python as it is simple and I have lots of experience
with it. It uses a couple of libraries:

  - Flask, as a webserver.
  - Bootstrap, for some nicely styled frontend.
  - PyJade, as an HTML templating engine.
  - Flake8 and extension, for code style checking.
  - Sendgrid, for the Python Sendgrid API
  - Mailgun, for the Python Mailgun API
  - Mandrill, for the Python Mandrill API
  - ses-mailer, for the Python Amazon SES API. I changed a little thing
    because the API seemed broken.

The only test that are done are style guide checks and checks to see if the
application starts and returns correct statuses for basic requests. No more
tests are done as actual testing of mails would require valid API keys in the
configuration and I'd rather not have mine public.

## Hosted application
The application is hosted here: http://uber-mailer.jeltef.nl/
Please use the access credentials provided in the email I sent.

## Other code I'm proud of
My main project I'm proud of is [PyLaTeX](https://github.com/JelteF/PyLaTeX),
which can be used to generate LaTeX with Python.

A Rust project I've been working on is
[derive_more](https://github.com/JelteF/derive_more), which extends the
automatically derivable traits in Rust with other common ones.

And lastly I have created an easy Python wrapper around Linux FUSE, called
[easyfuse](https://github.com/JelteF/easyfuse). With it you can create a
filesystem out of basically anything.

## Resume
My resume can be found here: http://uber-mailer.jeltef.nl/static/cv.pdf
