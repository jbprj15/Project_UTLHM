from django.shortcuts import render

def home(request):
    
    context = {}    
    template = "home.html"
    return render(request, template, context)

def aboutus(request):
    
    context = {}    
    template = "aboutus.html"
    return render(request, template, context)

def test(request):
    
    context = {}    
    template = "test.html"
    return render(request, template, context)
