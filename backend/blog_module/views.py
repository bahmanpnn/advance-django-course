from django.shortcuts import render


def index(request):
    context={
        "name":"bahman pournazari"
    }
    return render(request,'index.html',context)