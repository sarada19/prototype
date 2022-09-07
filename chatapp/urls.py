from django.urls import path
from .views import *

urlpatterns = [
    # Api View
    
    path('Api/list/', List_view.as_view()),

    # Project view
    path('', home, name= 'home'),
    path('add', create_post, name='add'),
    path('approve', admin_approve, name='approve'),
    path('Answer-Approve', admin_approve_answer, name='answer'),
    path('register', register, name='register'),
    path('login', signin , name= 'login'), 
    path('logout', signout, name='logout'),
]
