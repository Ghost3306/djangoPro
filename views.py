from django.shortcuts import render


def home(request):
    return render(request,"index.html")

def log(request):
    if request.method =="POST":
        username = request.POST['user']
        password = request.POST['pass']
        if(username==password):
            return render(request,"hello.html")