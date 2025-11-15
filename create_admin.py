import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courier.settings')
django.setup()

User = get_user_model()
username = "admin"
password = "admin123"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email="", password=password)
    print("✅ Admin user created successfully.")
else:
    print("⚠️ Admin user already exists.")
