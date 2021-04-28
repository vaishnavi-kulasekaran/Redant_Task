from django.shortcuts import render

# Create your views here. 	
from django.shortcuts import render
from .models import user_entries

def home(request):
	 all_users = user_entries.objects.all()
	 return render(request, 'home.html', {'all':all_users})