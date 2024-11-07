from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    # return HttpResponse("This is home page.")
    return render(request, "home.html")

def about(request):
    # return HttpResponse("This is about page.")
    return render(request, "about.html")


def projects(request):
    # return HttpResponse("This is projects page.")
    return render(request, "projects.html")


def contact(request):
    # return HttpResponse("This is contact page.")
    return render(request, "contact.html")
