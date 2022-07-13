from time import timezone
from webbrowser import get
from django.shortcuts import render

from .serializers import ProjectSerializer,ReviewsSerializer, TimeWorkedSerializer,UserSerializer,ActivitySerializer,ReportSerializer
from .models import Time_Worked, User,Project,Reviews,Activity
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from datetime import timedelta,datetime

# from prodev import serializers
# # from django.utils import timezone
# # Create your views here.
# class RegisterView(APIView):
    
#     def post(self,request):
#          serializer= UserSerializer(data=request.data)
#          serializer.is_valid(raise_exception=True)
#          serializer.save()
#          return Response(serializer.data)
     
# class LoginView(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = User.objects.filter(email=email).first()

#         if user is None:
#             raise AuthenticationFailed('User not found!')

#         # if not user.check_password(password):
#         #     raise AuthenticationFailed('Incorrect password!')

#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
#             'iat': datetime.datetime.utcnow()
#         }

#         token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

#         response = Response()

#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data = {
#             'jwt': token
#         }
#         return response
    
    
# class UserView(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
        
#         if not token:
#             raise AuthenticationFailed('Unauthenticated!')
        
#         try:
#             payload = jwt.decode(token, 'secret', algorithm=['HS256'])
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated!')
        
        
#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
# class LogoutView(APIView):
#     def post(self, request):
#         response = Response()
#         response.delete_cookie('jwt')
#         response.data = {
#             'message': 'success'
#         }
#         return response
        
        
    
        
        
        



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
#     def list(self, request):
#         queryset = Project.objects.all()
#         context = {
#             'queryset': queryset,
#         }
#         serializer = ProjectSerializer(queryset, many=True)
#         return Response(serializer.data,context)

#     def retrieve(self, request, pk=None):
#         queryset = Project.objects.all()
#         project = get_object_or_404(queryset, pk=pk)
#         serializer = ProjectSerializer(user)
#         return Response(serializer.data)
        
    
# # class TrialViewSet(viewsets.ModelViewSet,id):
# #      queryset = Project.objects.all().filter(id=id)
# #      serializer_class = ProjectSerializer    


class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
    
class ReviewsViewSet(viewsets.ModelViewSet):
     queryset = Reviews.objects.all()
     serializer_class = ReviewsSerializer
    
#########method 2################################################################################################################
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
       'List':'/project-list/',
       'DetailViewSet':'/project-detail/<str:pk>/',
       'Create':'/project-create/',
       'update':'/project-update/<str:pk>/',
       'Delete':'/project-delete/<str:pk>/',
    }
  
    return Response(api_urls)
@api_view(['GET'])
def projectList(request):
    projects = Project.objects.all() 
    serializer = ProjectSerializer(projects,many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def projectList_user(request,user_id):
    projects = Project.objects.filter(user=user_id) 
    serializer = ProjectSerializer(projects,many=True)  
    return Response(serializer.data)



@api_view(['GET'])
def projectDetail(request,id):
    projects = Project.objects.get(id = id) 
    serializer = ProjectSerializer(projects,many=False)  
    return Response(serializer.data)



@api_view(['POST'])
def projectCreate(request):
    
    serializer = ProjectSerializer(data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def projectUpdate(request,id):
    projects = Project.objects.get(id = id) 
    serializer = ProjectSerializer(instance=projects,data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def projectDelete(request,id):
    projects = Project.objects.get(id = id) 
    projects.delete()
    
    return Response('item successfully deleted')


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
       'List':'/user-list/',
       'DetailViewSet':'/user-detail/<str:pk>/',
       
       'update':'/user-update/<str:pk>/',
       
    }
  
    return Response(api_urls)


########user###############################
@api_view(['POST'])
def userUpdate(request,id):
    user = User.objects.get(id = id) 
    serializer = UserSerializer(instance=user,data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#################activity#################################################3

@api_view(['GET'])
def activityList(request):
    activities = Activity.objects.all() 
    serializer = ActivitySerializer(activities,many=True)  
    return Response(serializer.data)

@api_view(['GET'])
def activityList_user(request,user_id):
    activities = Activity.objects.filter(user=user_id) 
    serializer = ActivitySerializer(activities,many=True)  
    return Response(serializer.data)



@api_view(['GET'])
def activityDetail(request,id):
    activities= Activity.objects.get(id = id) 
    serializer = ActivitySerializer(activities,many=False)  
    return Response(serializer.data)



@api_view(['POST'])
def activityCreate(request):
    
    serializer = ActivitySerializer(data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['POST'])
def activityUpdate(request,id):
    activities = Activity.objects.get(id = id)
    serializer = ActivitySerializer(instance=activities,data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)



@api_view(['DELETE'])
def activityDelete(request,id):
    activities = Activity.objects.get(id = id) 
    activities.delete()
    
    return Response('item successfully deleted')

########################################## Dashboard ###############################################



@api_view(['GET'])
def get_statistics(request,user_id):
    projects = Time_Worked.objects.filter(user=user_id)
    daily_hours = Time_Worked.objects.filter(user=user_id)
    projects1 = Project.objects.filter(user=user_id)
    project_len = len(projects1)
    
    projects1 = projects.filter(date_added=datetime.strftime(datetime.now() - timedelta(0), '%Y-%m-%d'))
    projects2 = projects.filter(date_added=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'))
    projects3 = projects.filter(date_added=datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d'))
    projects4 = projects.filter(date_added=datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d'))
    projects5 = projects.filter(date_added=datetime.strftime(datetime.now() - timedelta(4), '%Y-%m-%d'))   

    serializer = ProjectSerializer(projects,many=True)  
    return Response({'no_of_projects':project_len,'daily_minutes':{
        'day_1': get_hours(projects1),
        'day_2': get_hours(projects2),
        'day_3': get_hours(projects3),
        'day_4': get_hours(projects4),  
        'day5':  get_hours(projects5),
    },
    'daily_hours': get_hours(projects1)+get_hours(projects2)+get_hours(projects3)+get_hours(projects4)+get_hours(projects5)
    })

def get_hours(projects):
    serializer = TimeWorkedSerializer(projects,many=True)
    minutes = 0
    for project in serializer.data:
        minutes = project['time_worked'] + minutes
    return minutes


@api_view(['GET'])
def time_worked_get(request,user_id):
        projects = Time_Worked.objects.all().filter(user=user_id)

        serializers = ReportSerializer(projects, many=True)

        return Response(serializers.data)


@api_view(['POST'])   
def time_worked_post(request):
        serializer = TimeWorkedSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
      
      
##############################################reportpage#######################################################################

@api_view(['GET'])  
def report_page(request,user_id):
    projects = Project.objects.filter(user=user_id) 
    all_projects =[]
    for project in projects:
        x = Time_Worked.filter(project=project.id)
    serializer = ProjectSerializer(projects,many=True)  
    return Response(serializer.data)

    
    
      



