from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="home"),
    path('blog',views.blog,name="blog"),
    path('contactus',views.contactus,name="contactus"),
    path('userlogin',views.userlogin,name="userlogin"),
    path('cat_post',views.cat_post,name="cat_post"),
    path('view_post',views.view_post,name="view_post"),
    path('readmore',views.readmore,name="readmore"),
    path('subscribe',views.subscribe , name="subscribe"),
    path('usersignup',views.usersignup , name="usersignup"),
    path('userpost',views.userpost, name="userpost"),
    path('logout',views.logout, name="logout")
]
