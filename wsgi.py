"""
WSGI entry point para servidores de produção (Gunicorn, uWSGI, etc.)
"""
from app import app

if __name__ == "__main__":
    app.run()
