from django.shortcuts import render

from configrations.models import SuccessStory, Logo, Service, Advantage, Goal


def index(request):
    stories = SuccessStory.objects.filter(is_active=True).order_by('-id')
    logos = Logo.objects.filter(is_active=True).order_by('-id')
    services = Service.objects.filter(is_active=True).order_by('-id')
    advantages = Advantage.objects.filter(is_active=True).order_by('-id')
    goals = Goal.objects.filter(is_active=True).order_by('-id')
    return render(request, 'index.html', {'stories': stories, 'logos': logos, 'services': services, 'advantages': advantages, 'goals': goals})
