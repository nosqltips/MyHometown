from django.http import HttpResponse, Http404
from django.urls import reverse
import qrcode

def event_code(request, pk):
    url = request.build_absolute_uri(reverse('public-event-detail', args=[pk]))
    img = qrcode.make(url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Set the box size to 10x10 pixels
        border=4,  # Set the border width to 4 pixels
    )
    img = qr.make_image()
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response

def project_code(request, pk):
    url = request.build_absolute_uri(reverse('public-project-detail', args=[pk]))
    img = qrcode.make(url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Set the box size to 10x10 pixels
        border=4,  # Set the border width to 4 pixels
    )
    img = qr.make_image()
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response

def crcclass_code(request, pk):
    url = request.build_absolute_uri(reverse('public-crcclass-detail', args=[pk]))
    img = qrcode.make(url)
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,  # Set the box size to 10x10 pixels
        border=4,  # Set the border width to 4 pixels
    )
    img = qr.make_image()
    response = HttpResponse(content_type='image/png')
    img.save(response, 'PNG')
    return response