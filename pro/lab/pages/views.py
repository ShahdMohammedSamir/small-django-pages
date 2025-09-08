from django.shortcuts import render # type: ignore
from .models import Login
from .form import LoginForm 
# Create your views here.
def home(request):
    return render(request,'pages/home.html')

def  about(request):
    return render(request,'pages/about.html')

##Method 1

# def form(request):
#     Login(request.POST).save()

#     return render(request, "pages/form.html",{'LF':LoginForm()})


##Method 2
# def form(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         Login.objects.create(username=username, password=password)

#     return render(request, "pages/form.html",{'LF':LoginForm()})


##Method 3
def form(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoginForm()

    return render(request, "pages/form.html", {"LF": form})