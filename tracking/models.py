from django.db import models

# Image model for packages
class PackageImage(models.Model):
    image = models.ImageField(upload_to='package_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"

# Shipment model
class Shipment(models.Model):
    TRACK_ID = models.CharField(max_length=100, unique=True)
    STATUS_CHOICES = [
        ('ORDER_PLACED', 'Order Placed'),
        ('LEFT_WAREHOUSE', 'Left Warehouse'),
        ('IN_TRANSIT', 'In Transit'),
        ('DELIVERED', 'Delivered'),
    ]
    STATUS = models.CharField(max_length=50, choices=STATUS_CHOICES, default='ORDER_PLACED')

    # Addresses
    ORIGIN_ADDRESS = models.CharField(max_length=255, default="Unknown")
    DISPATCH_OFFICE = models.CharField(max_length=255, default="Unknown")
    PICKUP_DATE = models.DateField(null=True, blank=True)
    DISPATCH_DATE = models.DateField(null=True, blank=True)
    DESTINATION_ADDRESS = models.CharField(max_length=255, default="Unknown")
    EXPECTED_DELIVERY_DATE = models.DateField(null=True, blank=True)

    # Sender
    SENDER_CONTACT_NAME = models.CharField(max_length=100, default="Unknown")
    SENDER_PHONE_NUMBER = models.CharField(max_length=50, default="Unknown")
    SENDER_CONTACT_ADDRESS = models.CharField(max_length=255, default="Unknown")
    SENDER_ORIGIN_CITY = models.CharField(max_length=100, default="Unknown")
    SENDER_COUNTRY = models.CharField(max_length=100, default="Unknown")

    # Receiver
    RECEIVER_CONTACT_NAME = models.CharField(max_length=100, default="Unknown")
    RECEIVER_PHONE_NUMBER = models.CharField(max_length=50, default="Unknown")
    RECEIVER_CONTACT_ADDRESS = models.CharField(max_length=255, default="Unknown")
    RECEIVER_ORIGIN_CITY = models.CharField(max_length=100, default="Unknown")
    RECEIVER_COUNTRY = models.CharField(max_length=100, default="Unknown")

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.TRACK_ID

# Package model
class Package(models.Model):
    shipment = models.ForeignKey(Shipment, related_name='packages', on_delete=models.CASCADE)
    PACKAGE_NAME = models.CharField(max_length=255, default="Package")
    PACKAGE_WEIGHT = models.PositiveIntegerField(default=0)
    PACKAGE_QUANTITY = models.PositiveIntegerField(default=1)
    images = models.ManyToManyField(PackageImage, blank=True)

    def __str__(self):
        return self.PACKAGE_NAME
