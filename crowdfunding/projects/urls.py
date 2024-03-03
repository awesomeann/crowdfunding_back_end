from django.urls import path
from . import views

urlpatterns = [
    path('projects/', views.ProjectList.as_view()),
    path('', views.ProjectList.as_view()),
    path('projects/<int:pk>/', views.ProjectDetail.as_view()),
    path('pledges/<int:project_id>', views.PledgeList.as_view()),
    # path('pledges/<int:pk>/', views.PledgeDetail.as_view()),
    path('pledges/', views.PledgeList.as_view()),
    path('projects-status/<int:pk>/', views.ProjectStatus.as_view()),

]