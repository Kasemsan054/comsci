from django.shortcuts import render, redirect
from django.http import HttpResponse
from testapp.models import Person

# Create your views here.
def index(request):
    all_person = Person.objects.all()
    return render(request, "index.html", {"all_person": all_person})

def about(request):
    return render(request, "about.html")

def form(request):
    if request.method == "POST":
        name = request.POST["name"]
        age = request.POST["age"]

        person = Person.objects.create(
            name = name,
            age = age,
        )
        person.save()
        return redirect("/")
    else :    
        return render(request, "form.html")

def error(request):
    return render(request, "404.html")