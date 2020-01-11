from django.conf.urls import url
#from . import views
from django.urls import path
from .views import KeibaView, horse_db, create,edit

urlpatterns = [
    url('index', KeibaView.as_view(), name='index'),
    url('horse', horse_db, name='horse'),
    url('create', create, name='create'),
    path('edit/<int:num>', edit, name='edit'),
    url('edit/', edit, name='edit'),
    #url('delete/<int:num>', delete,name='delete')
    #url('index', views.index, name='index'),
    #url('next', views.next, name='next'),
    #url('form', views.form, name='form'),
]
