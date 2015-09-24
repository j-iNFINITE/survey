from django.conf.urls import patterns,url
from survey import views
urlpatterns = patterns('',
                       url(r'^search/',views.search, name='search'),
                       url(r'^form/',views.form,name='form'),
                       url(r'^done',views.done,name='done'),
                       url(r'$',views.index,name='index'),
                       )
