from django.conf.urls import url
from . import views

app_name = 'form'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user-form/$', views.user_form, name='user_form'),
    ]