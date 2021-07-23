from django.urls import path
from django.conf.urls import url
from . import views
from .views import home,matlablistuser,signup,log_in,log_out,contact,panel,addmatlab,searchmatlabs,editmatlab,deletematlab,homematlab,detail

urlpatterns = [
    path('',homematlab,name="home"),
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path("contact/", contact, name="contact"),
    path("panel/", panel, name="panel"),
    path("addmatlab/", addmatlab, name="addmatlab"),
    path("matlabs/", searchmatlabs, name="searchmatlabs"),
    path("mymatlabs/", matlablistuser , name="matlabslistuser"),
    path(r'editmatlab/(?P<id>)', editmatlab , name="editmatlab"),
    path(r'deletematlab/(?P<id>)', deletematlab , name="deletematlab"),
    url(r'^(?P<id>[0-9]{1,3})$', views.detail , name='detail'),
]