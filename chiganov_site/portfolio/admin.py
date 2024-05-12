from django.contrib import admin
from .models import Portfolio
from .forms import PortfolioForm

# Register your models here.

class PortfolioAdmin(admin.ModelAdmin):
    form = PortfolioForm

admin.site.register(Portfolio, PortfolioAdmin)