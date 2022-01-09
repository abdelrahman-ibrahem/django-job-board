from django.urls import path 
from . import views
app_name = 'main'


urlpatterns = [
    path('' , views.home , name="home"),
    path('jobs/' , views.job_page , name="job_page"),
    path('contact/' , views.contact , name="contact"),
    path('login/' , views.login_page , name="login"),
    path('register/' , views.register_page , name="register"),
    path('logout_page/' , views.logout_page , name="logout"),
    path('add_job/' , views.add_job , name="add_job"),
    path('profile_page/' , views.profile_page , name="profile"),
    path('jon_detail/<slug:slug>' , views.job_detail , name="job_detail")
]