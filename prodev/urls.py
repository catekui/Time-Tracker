from django.urls import path,include
from rest_framework import routers
from . import views

# from .views import *

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'Project', views.ProjectViewSet)
router.register(r'reviews', views.ReviewsViewSet)
# router.register(r'<id>', views.TrialViewSet)
urlpatterns = [
    path('',include(router.urls)),
    path('home/', views.ApiOverview, name='home'),
    path('api/auth',include('rest_framework.urls')),
    path('project-list', views.projectList, name='project-list'),
    path('project-list/<str:user_id>/', views.projectList_user),
    path('project-detail/<str:id>/', views.projectDetail, name='project-detail'),
    path('project-create', views.projectCreate, name='project-create'),
    path('project-update/<str:id>/', views.projectUpdate, name='project-update'),
    path('project-delete/<str:id>/', views.projectDelete, name='project-delete'),
]