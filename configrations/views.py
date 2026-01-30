from django.shortcuts import render
from .models import SuccessStory

def index(request):
    stories = SuccessStory.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'index.html', {'stories': stories})
