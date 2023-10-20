from django.shortcuts import render


# Create your views here.
def prf(request):
    return render(request, 'prf/prf.html')
