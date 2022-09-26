from django.shortcuts import render


def index(request):
    context = {}
    return render(request,'aboutme/index.html',context)
