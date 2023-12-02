from django.urls import path
# from .import views
from .import views


urlpatterns = [
    path('',views.Home_portfolio, name= "home"),
    path('About',views.about_me, name= "about"),
    path('Resume',views.my_resume, name= "resume"),
    path('Contact',views.my_contact, name= "contact"),
    path('Portfolio',views.my_portfolio, name= "portfolio"),
    path('Header',views.header, name= "header"),
    path('Projects',views.projects, name= "projects"),
    path('Submit-Contact',views.submit_contact, name= "submitContact"),

    path('OnlinePortfolio',views.online_portfolio, name= "onlinePort"),
    path('OnAbout',views.online_about, name= "onAbout"),
    path('OnServices',views.online_Services, name= "onServices"),
    path('OnPortfolio',views.online_Portfolio, name= "onPortfolio"),
    
    path('datatable', views.datatable_view, name='datatable'),
    path('checkContact', views.checked_contact, name='checkContact'),
    path('deleteContact', views.delete_contact, name='deleteContact'),
    
]