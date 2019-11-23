from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^create/$',views.new_contact,name='new_contact'),
    url(r'^contact/(?P<contact_id>\d+)/$',views.contact,name='view_contact'),
    url(r'^(?P<contact_id>\d+)/$',views.contact),
    url(r'^all/$',views.view_contacts,name='view_contacts'),
    url(r'^$',views.view_contacts),
    url(r'^contact/(?P<contact_id>\d+)/update/$',views.update_contact,name='update_contact'),
    url(r'^contact/(?P<contact_id>\d+)/delete/$',views.delete_contact,name="delete_contact")
]