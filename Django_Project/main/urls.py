from django.conf.urls import url
from main import views

# Template Tagging 
app_name="main"

urlpatterns = [
	#url('admin/', admin.site.urls),#
	
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^components/$', views.components, name='components'),
	url(r'^work/$', views.work, name='work'),
	url(r'^works/$', views.works, name='works'),	
]