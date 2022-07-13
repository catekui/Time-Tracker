from .serializers import ProjectSerializer, TimeWorkedSerializer,ActivitySerializer,ProfileSerializer,ReviewsSerializer,UserSerializer1
from .models import Time_Worked,Project,Reviews,Activity,User
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import timedelta,datetime

    
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ActivityViewSet(viewsets.ModelViewSet):
    queryset = Activity.objects.all()
    serializer_class = ActivitySerializer
    
    
class ReviewsViewSet(viewsets.ModelViewSet):
     queryset = Reviews.objects.all()
     serializer_class = ReviewsSerializer

class UserViewSet(viewsets.ModelViewSet):
     queryset = User.objects.all()
     serializer_class = UserSerializer1
    
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
def profileUpdate(request,id):
    user = User.objects.get(id = id) 
    serializer = ProfileSerializer(instance=user,data=request.data)  
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


#################activity#################################################3
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
    statistics = Time_Worked.objects.filter(user=user_id)
    daily_hours = Time_Worked.objects.filter(user=user_id)
    projects1 = Project.objects.filter(user=user_id)
    project_len = len(projects1)
    
    projects1 = statistics.filter(date_added=datetime.strftime(datetime.now() - timedelta(0), '%Y-%m-%d'))
    projects2 = statistics.filter(date_added=datetime.strftime(datetime.now() - timedelta(1), '%Y-%m-%d'))
    projects3 = statistics.filter(date_added=datetime.strftime(datetime.now() - timedelta(2), '%Y-%m-%d'))
    projects4 = statistics.filter(date_added=datetime.strftime(datetime.now() - timedelta(3), '%Y-%m-%d'))
    projects5 = statistics.filter(date_added=datetime.strftime(datetime.now() - timedelta(4), '%Y-%m-%d'))   
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

      
##############################################reportpage#######################################################################
@api_view(['GET'])
def time_worked_get(request,user_id):
        projects = Time_Worked.objects.all().filter(user=user_id)
        serializers = TimeWorkedSerializer(projects, many=True)
        return Response(serializers.data)



########################### Timer after ikimalizia ############################################################################
@api_view(['POST'])   
def time_worked_post(request):
        serializer = TimeWorkedSerializer(data=request.data)  
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
      


    
    
      
