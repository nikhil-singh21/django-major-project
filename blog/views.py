from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .models import *
import json
from django.conf import settings
from django.conf.urls.static import static



# Create your views here.
def index(request):
    return render(request,'blog/home.html')

def blog(request):
    c=Category.objects.all()
    p=Post.objects.all()
    return render(request,'blog/blog.html',{'post':p,'cat':c})

def contactus(request):
    if request.method == 'GET':
         return render(request,'blog/contact.html')
    elif request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.contact_no = request.POST.get('contactno')
        contact.email_id = request.POST.get('email')
        contact.query = request.POST.get('query')
        contact.save()
        masg="success"
        return render(request,'blog/contact.html')
    else:
        return render(request,'blog/contact.html')       

def userlogin(request):
    if request.method == 'GET':
        return render(request,'blog/login.html')
    elif request.method == 'POST':
        if Usersignup.objects.filter(username=request.POST.get('username'),password=request.POST.get('password')):
            name=Usersignup.objects.filter(username = request.POST.get('username') )[0]
            post = Post.objects.all()
            return render (request,'blog/Admintemplate.html',{'name':name,'post':post})
        else:
            return HttpResponse("invalid id")      


def usersignup(request):
    if request.method == 'GET':
        return render(request,'blog/usersignup.html')
    elif request.method == 'POST':
        signup = Usersignup()
        signup.username = request.POST.get('username')
        signup.name = request.POST.get('name')
        signup.Contactno = request.POST.get('contactno')
        signup.password = request.POST.get('password')
        signup.save()
        return render(request,'blog/usersignup.html')
    else:
         return render(request,'blog/usersignup.html')
    
def userpost(request):
    if request.method == 'GET':
        user_id = request.GET.get('user_id')
        if user_id :
            user_id = user_id
            post = Post.objects.filter(username = user_id).all()
            return render (request,'blog/post.html',{'post':post})
        else:
            return HttpResponse("error")        

def logout(request):
    return render(request,'blog/login.html')

        

def cat_post(request):
    cat_id=request.GET.get('cat_id')
    if cat_id:
        cat_id=int(cat_id)
        post=Post.objects.filter(id=cat_id).all()
        cat=Category.objects.all()
        return render(request,'blog/blog.html',{'post':post,'cat':cat})
    else:
        return HttpResponse('error')

def view_post(request):
    post_id=request.GET.get('post_id')
    if post_id:
        post_id=int(post_id)
        post=Post.objects.filter(id=post_id).all()
        cat=Category.objects.all()
        post=json.load(post)
        return render(request,'blog/blog.html',{'post':post,'cat':cat})
 
def readmore(request):
    post_id=request.GET.get('post_id')
    if post_id:
        post_id =int(post_id)
        post=Post.objects.filter(id=post_id).all()
        return render(request,'blog/readmore.html',{'post':post})
    else:
        return HttpResponse('error')



def subscribe(request):
    if request.method == 'GET':
        return render(request,'blog/contact.html')
    elif request.method == 'POST':
        subs = Subscription()
        subs.email_id= request.POST.get('email')
        subs.save()
        return render(request,'blog/contact.html')            
    else:
        return HttpResponse("error")    

