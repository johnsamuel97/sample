from django.contrib import admin
from django.urls import path,include
from website import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Home_view, name='home'),
    #path('login/', views.Login_view, name='login'),
    path('about/', views.AboutUs_view, name='about'),
    path('reg/', views.Register_view, name='reg'),
    path('data', views.Data_view, name='data'),
    path('logout', views.Logout_view, name='logout'),
    path('signup', views.Signup_view, name='signup'),
    path('record/<int:id>/', views.customer_record, name='record'),
    path('delete/<int:id>/', views.delete_record, name='delete'),
    path('update/<int:id>/', views.update_record, name='update'),
    path('insert/', views.insert_view, name='insert'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('tech/', views.Tech, name='tech'),
    ]
