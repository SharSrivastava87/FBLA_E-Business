from django.urls import path
from register.views import login_view
app_name = 'register'

urlpatterns=[
    path('login/', login_view, name='login'),

]