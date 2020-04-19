from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from webssh.ssh_tools import unique
from zlssh.settings import TMP_DIR

import os


def index(request):
    return render(request, 'webssh.html')

def history(request):
    return render(request, 'record.html')

def upload_ssh_key(request):
    if request.method == 'POST':
        pkey = request.FILES.get('pkey')
        ssh_key = pkey.read().decode('utf-8')

        while True:
            filename = unique()
            ssh_key_path = os.path.join(TMP_DIR, filename)
            if not os.path.isfile(ssh_key_path):
                with open(ssh_key_path, 'w') as f:
                    f.write(ssh_key)
                break
            else:
                continue

        return HttpResponse(filename)
