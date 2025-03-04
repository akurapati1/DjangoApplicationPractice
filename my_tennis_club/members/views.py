from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import members as mb

def members(request):
    mymembers = mb.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers' : mymembers,
    }

    return HttpResponse(template.render(context, request))

# Create your views here.
