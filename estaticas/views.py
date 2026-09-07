from django.shortcuts import render

def mostrar_home(request):
    return render(request, 'index.html')

def mostrar_about(request):
    return render(request, 'about.html')

def mostrar_acerca(request):
    datos = {
        "wifi" : "300mbps" ,
        "enchufes" : 10,
        "cafe" : "tostado",
        "ambiente" : "silencioso"
    }
    return render(request, 'about.html',datos)