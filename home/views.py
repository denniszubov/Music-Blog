from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        "page": "HOME!"
    }
    return render(request, "home/home.html", context)
