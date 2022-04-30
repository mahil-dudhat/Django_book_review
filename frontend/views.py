from django.shortcuts import render


# Create your views here.

def home(request):    
     return render(request, 'frontend_templates/index.html')

def public(request):    
     return render(request, 'frontend_templates/public.html')

def personal(request):    
     return render(request, 'frontend_templates/personal.html')