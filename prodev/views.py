from django.shortcuts import render

from .serializers import ProjectSerializer,ReviewsSerializer,UserSerializer,ActivitySerializer
from .models import User,Project,Reviews,Activity
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime

# Create your views here.
class RegisterView(APIView):
    
    def post(self,request):
         serializer= UserSerializer(data=request.data)
         serializer.is_valid(raise_exception=True)
         serializer.save()
         return Response(serializer.data)
     
class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
         
         
        user = User.objects.filter(email=email).first()
        
        if user is None:
            raise AuthenticationFailed('user not found')
       
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }
        
        token = jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')#token
        
        response = Response()
        
        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }
        
        return response
    
    
class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')
        
        if not token:
            raise AuthenticationFailed('Unauthenticated!')
        
        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')
        
        
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
        
        
    
        
        
        



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

