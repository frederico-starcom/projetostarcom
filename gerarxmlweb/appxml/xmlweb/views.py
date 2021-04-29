from django.shortcuts import render


# Create your views here.

def index(request):
    context = {
        'loading': 'test'
    }
    return render(request, 'xmlweb/index.html', context)
