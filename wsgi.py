import os
from django.core.wsgi import get_wsgi_application

# Set the Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'povalogistics.settings')

# Define the application variable
application = get_wsgi_application()  # This is the WSGI application Vercel needs
