from django.shortcuts import HttpResponse, render
import qrcode
from django.conf import settings
import os
from io import BytesIO

def home(request):
    return render(request,"index.html")
def generate_QR(request):
    if request.method == "POST":
        upi_id = request.POST.get("upi_id")

        # Define the payment URL based on the UPI ID
        url = f"upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234"

        # Generate the QR Code
        phonepe_qr = qrcode.make(url)

        # Save QR Code to a BytesIO stream
        buffer = BytesIO()
        phonepe_qr.save(buffer, format="PNG")
        buffer.seek(0)

        # Return QR Code as an HTTP response with image/png content type
        return HttpResponse(buffer, content_type="image/png")

     