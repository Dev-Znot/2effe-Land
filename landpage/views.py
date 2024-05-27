from django.shortcuts import render, redirect
from django.contrib import messages

from .models import LandModel
from .form import LandForm


def landpage(request):
    if request.method == "GET":
        form = LandForm()

        context = {
            "form":form
        }

        return render(request, "landpage/index.html", context)
    
    elif request.method == "POST":
        form = LandForm(request.POST)

        if form.is_valid():
            form.save()

            return render(request, "landpage/index.html", {"sucesso": True, 'form': form})
        else:
            return render(request, 'landpage/index.html', {'form': form})
        



