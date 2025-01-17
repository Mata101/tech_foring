from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# models
from ..models import Projects,ProjectMembers
from django.contrib.auth.models import User


# Create your views here.
    
@api_view(['GET','PUT','PATCH','DELETE'])
def delete_update_get_project(request,project_id):
    
    #update a project
    if request.method == 'PUT' or request.method == 'PATCH':
        try:
            data = {}
            for i in request.POST:
                data[i]=request.POST[i]

            Projects.objects.filter(pk=project_id).update(**data)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    
    #delete project
    if request.method == 'DELETE':
        try:
            Projects.objects.filter(pk=project_id).delete()
            return Response('Project deleted.',status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_404_NOT_FOUND)
        
    #return specific project
    try:
        project = Projects.objects.values('id','name', 'description', 'owner','created_at').get(pk=project_id)
        return Response({'data':project},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST','GET'])
def create_project(request):
    #creating a project
    if request.method == 'POST':
        try:
            data = {}
            for i in request.POST:
                if i == 'owner':
                    data[i]=User.objects.get(pk=request.POST.get('owner'))
                else:

                    data[i]=request.POST[i]
            Projects.objects.create(**data)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        
    #return project list
    return Response({ 'data': Projects.objects.values('id','name', 'description', 'owner','created_at') },status=status.HTTP_200_OK)