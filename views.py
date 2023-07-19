from django.shortcuts import render ,get_object_or_404, redirect
from.models import *
from django.http import HttpResponse
from django.core.paginator import Paginator
# from .serializers import NotesSerializer
# from rest_framework.generics import ListAPIView


# Create your views here.


 
def insertdata(request):
    if request.method== "POST":
        data = request.POST

        notesdata = data.get('notesdata')
       
        Notes.objects.create(
            notesdata = notesdata,
          
        )
        return redirect('/home/') 
    queryset = Notes.objects.all()
    page_obj = ''
    
    context = {}
    i = 1 
      
    if request.GET.get('search'):
        queryset = queryset.filter(notesdata__icontains =request.GET.get('search'))
    elif len(queryset)==0:
            return redirect('/home/')
        
    paginator  = Paginator(queryset,5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'home':page_obj}  
   
    
    return render(request , "home.html" , context )


def delete_notes(request,id):
     queryset = Notes.objects.get(id=id)
    #  if request.method == 'POST':
     queryset.delete()
     return redirect('/home/')
    #  context = {'queryset':queryset}
     
    #  return render(request,'delete_notes.html',context)
 


def update_notes(request,id):
    queryset = Notes.objects.get(id=id)

    if request.method == "POST":
     data = request.POST

     notesdata = data.get('notesdata')
    #  idname = data.get('idname')


     queryset.notesdata = notesdata
    #  queryset.idename = idname
     queryset.save()
     return redirect('/home/')

    context = {'data':queryset}
    return render(request, 'update_notes.html' , context)

