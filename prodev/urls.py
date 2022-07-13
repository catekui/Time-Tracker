from django.urls import path,include
from rest_framework import routers
from . import views
from .auth import RegisterView,LoginView,UserView,LogoutView



# from .views import *

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'Project', views.ProjectViewSet)
router.register(r'reviews', views.ReviewsViewSet)
router.register(r'activity', views.ActivityViewSet)

# router.register(r'<id>', views.TrialViewSet)
urlpatterns = [
    
    path('',include(router.urls)),
    path('register',RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('kid', UserView.as_view()),
    path('logout', LogoutView.as_view()),    
    path('home/', views.ApiOverview, name='home'),
    path('api/auth',include('rest_framework.urls')),
    path('project-list', views.projectList, name='project-list'),
    path('project-list/<str:user_id>/', views.projectList_user),
    path('project-detail/<str:id>/', views.projectDetail, name='project-detail'),
    # path('project-time/<time_interval>/', views.projecttime, name='project-time'),
    path('project-create', views.projectCreate, name='project-create'),
    path('project-update/<str:id>/', views.projectUpdate, name='project-update'),
    path('project-delete/<str:id>/', views.projectDelete, name='project-delete'),
    path('user-update/<str:id>/', views.userUpdate, name='user-update'),    
    path('activity-list', views.activityList, name='activity-list'),
    path('activity-list/<str:user_id>/', views.activityList_user),
    path('activity-detail/<str:id>/', views.activityDetail, name='activity-detail'),
    # path('project-time/<time_interval>/', views.projecttime, name='project-time'),
    path('activity-create', views.activityCreate, name='activity-create'),
    path('activity-update/<str:id>/', views.activityUpdate, name='activity-update'),
    path('activity-delete/<str:id>/', views.activityDelete, name='activity-delete'),
    # path('activity-update/<str:id>/', views.userUpdate, name='user-update'),
    path('get_statistics/<str:user_id>/', views.get_statistics, name='get_statistics'),
    path('time_worked_get/<str:user_id>/', views.time_worked_get, name='get_time_worked'),
    path('time_worked_post/', views.time_worked_post, name='get_time_worked'),

]