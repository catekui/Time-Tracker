from django.shortcuts import render

from .serializers import ProjectSerializer,ReviewsSerializer,UserSerializer
from .models import User,Project,Reviews
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

# Create your views here.

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
