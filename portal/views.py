from django.http import request
from django.shortcuts import render

from .models import Person, Publish1, Publish, Time_Test

from portal import forms, models


# Create your views here.

def index(request):
    queryset = Publish.objects.all()
    context = {
       'object_list2': queryset
        }
    return render(request, 'portal/index.html', context)


def Register(request):

  form_data=forms.UserRegister(request.POST or None)
  msg=''
  if form_data.is_valid():
       person_data				    = models.Person()
       person_data.first_name	= form_data.cleaned_data['first_name']
       person_data.last_name	= form_data.cleaned_data['last_name']
       person_data.tlf			  = form_data.cleaned_data['tlf']
       person_data.e_post		  = form_data.cleaned_data['e_post']

       person_data.save()
       msg='data is saved'
       form_data=forms.UserRegister()

  context={
        'form':form_data,
        'msg':msg
    }
  return render(request,'portal/register.html',context)


def calendar(request):


  time_data = forms.Time_Test(request.POST or None)
  if time_data.is_valid():
       person_data             = models.Time_Test()
       person_data.title       = time_data.cleaned_data['title']
       person_data.date_test   = time_data.cleaned_data['date_test']
       person_data.bydel = time_data.cleaned_data['bydel']
       person_data.ham = time_data.cleaned_data['ham']

       person_data.save()
       
       time_data=forms.Time_Test()

  queryset = Time_Test.objects.all()


  context={
        'table': queryset,
        'form': time_data,


    }


  return render(request,'portal/calendar.html',context)


def Hei(request):
    queryset = Publish.objects.all()
    product  = Publish1.objects.all()
    persons  = Person.objects.all()

    context = {
       'object_list2': queryset,
       'object_list3': product,
       'object_list1': persons
       
        }
    
    return render(request, 'portal/sndex.html', context)
