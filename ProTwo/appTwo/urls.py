from django.conf.urls import url
from appTwo import views

urlpatterns = [
    # url(r'^help/',views.help,name='help'),
    url(r'^$',views.user,name='user'),
    # # url(r'^user/',views.user,name='user'),
    # url(r'^help/',views.help,name='help'),
    # url(r'^$',views.index,name='index'),
]
