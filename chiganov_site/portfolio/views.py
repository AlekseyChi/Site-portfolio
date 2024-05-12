from django.shortcuts import render, HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def home(request):
    return render(request, "portfolio/Light-portfolio/home.html")

def about(request):
    return render(request, "portfolio/Light-portfolio/about-us.html")
    
def portfolio(request):
    return render(request, "portfolio/Light-portfolio/portfolio.html")
    
def news(request):
    return render(request, "portfolio/Light-portfolio/news.html")
    
def contacts(request):
    return render(request, "portfolio/Light-portfolio/contact-us.html")
    
def users(request):
    return HttpResponse(f'Users: {User.get_full_name(request.user)}')