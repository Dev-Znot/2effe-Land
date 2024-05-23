from django.shortcuts import render, redirect


def landpage(request):
    return render(request, "landpage/index.html")
