from django.urls import path

from . import views

urlpatterns = [
    path('', views.logi, name='login'),
    path('logout/', views.logo, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/candidate/', views.create_candidate, name='create_candidate'),
    path('edit/candidate/<int:cid>/', views.update_candidate, name='edit_candidate'),
    path('view/candidate/<int:cid>/', views.view_candidate, name='view_candidate'),
    path('all/candidate/', views.all_candidate, name='all_candidate'),

]