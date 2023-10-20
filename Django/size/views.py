from django.shortcuts import render


# Create your views here.
def size(request):
    return render(request, 'size/size.html')
