from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from blog.models import Person

# Create your views here.
def index(request,rowid=""):
    if rowid:
         Person.objects.filter(id=rowid)[0].delete()
       
    name=request.GET.get('name','')
    age=request.GET.get('age','')
    gender=request.GET.get('gender','')
    file=request.GET.get('file','')
    if name == '' or age == '' or gender == '' :
        pass
    else:
        a=Person(name=name,age=age,gender=gender,image=file)
        a.save()
    person=Person.objects.all()
    return render(request,"blog/home.html",{'data':person})

def delete(request,rowid):
    rowid=request.GET.get('id')
    Person.objects.filter(id=rowid)[0].delete()
    person=Person.objects.all()
    return HttpResponse("delted")
    