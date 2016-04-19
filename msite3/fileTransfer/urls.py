from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'create/', views.create, name='create'),
	url(r'about/', views.about, name='about'),
        url(r'Sender/', views.SenderView.as_view(), name='Sender'),
]
