from django.contrib import admin
from .models import Shipment, Package, PackageImage

class PackageInline(admin.TabularInline):
    model = Package
    extra = 1

@admin.register(Shipment)
class ShipmentAdmin(admin.ModelAdmin):
    list_display = ("TRACK_ID", "STATUS", "SENDER_CONTACT_NAME", "RECEIVER_CONTACT_NAME", "DISPATCH_DATE", "EXPECTED_DELIVERY_DATE")
    list_filter = ("STATUS",)
    inlines = [PackageInline]

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ("PACKAGE_NAME", "PACKAGE_WEIGHT", "PACKAGE_QUANTITY", "shipment")

@admin.register(PackageImage)
class PackageImageAdmin(admin.ModelAdmin):
    list_display = ("id", "uploaded_at")
