from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Member
from django.urls import reverse

# Create your views here.
def index(request):
    mymembers=Member.objects.all().values()
    template=loader.get_template('index.html')
    context={
        'mymembers':mymembers,
    }
    
    return HttpResponse(template.render(context, request))
    
def add(request):
    template=loader.get_template('add.html')

    return HttpResponse(template.render({}, request))

def addrecord(request):
    x=request.POST['first']
    y=request.POST['last']
    member=Member(firstname=x, lastname=y)
    member.save()

    return HttpResponseRedirect(reverse('index'))

def delete(request, id):
    member=Member.objects.get(id=id)
    member.delete()
    
    return HttpResponseRedirect(reverse('index'))