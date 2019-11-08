from django.conf.urls import url
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^new_contact/$',views.new_contact,name='new_contact'),
    url(r'^view_contacts/$',views.view_contacts,name='view_contacts'),
    url(r'^update/$',views.update_contact,name='update'),
    url(r'^delete/$',views.delete_contact,name="delete")
]

#(?P<contact_id>[\d]+)