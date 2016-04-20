from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.main, name='main'),
	url(r'create/', views.create, name='create'),
	url(r'about/', views.about, name='about'),
        url(r'transfer/', views.TransferView.as_view(), name='transfer'),
	url(r'list/', views.list, name='list'),
	url(r'wrongPassword/', views.wrongPassword, name='wrongPassword'),
        url(r'sending/', views.send, name="send"),
        url(r'receiving/', views.receive, name="receive"),
    url(r'^login/$', 'django.contrib.auth.views.login', {
    'template_name': 'fileTransfer/login.html'
	}),

    url(r'^logout/$', 'django.contrib.auth.views.logout'),
]
