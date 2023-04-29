from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('create_assignment/', views.create_assignment, name='create_assignment'),
    path('assignment_list/', views.assignment_list, name='assignment_list'),
    path('company_login/', auth_views.LoginView.as_view(template_name='jurrmarketplace/company_login.html'), name='company_login'),
    path('company_logout/', auth_views.LogoutView.as_view(), name='company_logout'),
    path('company_register/', views.company_register, name='company_register'),  # Add this line
    path('lawyer_login/', auth_views.LoginView.as_view(template_name='jurrmarketplace/lawyer_login.html'), name='lawyer_login'),
    path('lawyer_logout/', auth_views.LogoutView.as_view(), name='lawyer_logout'),  # Add this line
    path('lawyer_register/', views.lawyer_register, name='lawyer_register'),
    path('apply_for_assignment/<int:assignment_id>/', views.apply_for_assignment, name='apply_for_assignment'),
    # Add this line
]
