"""Basic file to run the development server."""

from flask_failsafe import failsafe


@failsafe
def create_app():
    """Flask-Failsafe wrapper to allow better auto-reload."""
    from app import app

    return app

if __name__ == '__main__':
    create_app().run()
