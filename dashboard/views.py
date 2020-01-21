import io

from django.http import JsonResponse, FileResponse
from django.shortcuts import render

import ipfshttpclient

from topfile.settings import INFURA_URL, INFURA_PROJECT

client = ipfshttpclient.connect(INFURA_URL)


def dashboard(request):
    ctx = {
        'INFURA_PROJECT': INFURA_PROJECT
    }
    return render(request, 'home.html', context=ctx)


def get_files(request, address):
    return JsonResponse({
        'private': [],
        'public': []
    })


def upload_file(request):
    path = request.POST.get('filepath')
    file = request.FILES['file']
    client.add()
    pass


def get_file(request, file):
    bytes = client.cat(file)
    file = io.StringIO(bytes)

    return FileResponse(file)