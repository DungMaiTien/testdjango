from contextlib import redirect_stderr
from multiprocessing import context

from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render


# Create your views here.
def login2(request):
    error = ''
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        is_auth = authenticate(username=username,password=password)
        if is_auth:
            login(request,is_auth)
            request.session['username'] = username
            return redirect("product1:product1")
        else:
            error = "Sai tài khoản hoặc mật khẩu"
    
    context = {
        "error": error 
    }
        
    return render(request,'login2/login.html',context)