from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#models
from ..models import Tasks,Projects
from django.contrib.auth.models import User

@api_view(['GET','POST'])
def project_tasks(request,project_id):
    try:
        #create task
        if request.method == 'POST':
            try:
                data = {}
                for i in request.POST:
                    if i == 'assigned_to':
                        data[i]=User.objects.get(pk=request.POST.get('assigned_to'))
                    else:

                        data[i]=request.POST[i]
                data['project']=Projects.objects.get(pk=project_id)
                Tasks.objects.create(**data)
            except Exception as e:
                return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
            
        #return task list
        return Response({ 'data': Tasks.objects.values('id','title','description','status','priority','assigned_to','created_at','due_date','project').filter(project=project_id) },status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)

        

@api_view(['GET','PUT','PATCH','DELETE'])
def task(request,task_id):
    try:
        if request.method == "PUT" or request.method == "PATCH":
            try:
                data = {}
                for i in request.POST:
                    if i == 'assigned_to':
                        data[i]=User.objects.get(pk=request.POST.get('assigned_to'))
                    elif i == 'project':
                        data[i]=Projects.objects.get(pk=request.POST.get('project'))
                    else:

                        data[i]=request.POST[i]

                Tasks.objects.filter(pk=task_id).update(**data)
            except Exception as e:
                return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            try:
                Tasks.objects.filter(pk=task_id).delete()
                return Response('Task deleted.',status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e),status=status.HTTP_404_NOT_FOUND)
        return Response({'data': Tasks.objects.values('id','title','description','status','priority','assigned_to','created_at','due_date','project').get(pk=task_id)},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e),status=status.HTTP_404_NOT_FOUND)