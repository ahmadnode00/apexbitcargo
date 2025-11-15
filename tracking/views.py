from django.shortcuts import render
from .models import Shipment

def home(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")

def services(request):
    return render(request, "services.html")

# Tracking form page
def tracker_form(request):
    return render(request, "tracker.html")

# Tracking result page
def tracking_result(request):
    # get ?id=...
    track_id = request.GET.get("id")

    # if no ID given
    if not track_id:
        return render(request, "tracking_result.html", {
            "shipment": None,
            "packages": None,
            "step_names": ["Order Placed", "Left Warehouse", "In Transit", "Delivered"],
            "current_step": 0,
            "message": "Please enter a tracking number."
        })

    # find shipment
    shipment = Shipment.objects.filter(TRACK_ID__iexact=track_id).first()

    if not shipment:
        # no match
        return render(request, "tracking_result.html", {
            "shipment": None,
            "packages": None,
            "step_names": ["Order Placed", "Left Warehouse", "In Transit", "Delivered"],
            "current_step": 0,
            "message": f"No shipment found for Track ID: {track_id}"
        })

    # get packages
    packages_qs = shipment.packages.all()
    packages = packages_qs if packages_qs.exists() else None

    # progress bar mapping
    status_to_step = {
        "ORDER_PLACED": 1,
        "LEFT_WAREHOUSE": 2,
        "IN_TRANSIT": 3,
        "DELIVERED": 4,
    }
    shipment_status = (shipment.STATUS or "").upper()
    current_step = status_to_step.get(shipment_status, 1)

    return render(request, "tracking_result.html", {
        "shipment": shipment,
        "packages": packages,
        "step_names": ["Order Placed", "Left Warehouse", "In Transit", "Delivered"],
        "current_step": current_step,
        "message": None,
    })
