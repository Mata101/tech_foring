from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

#models
from ..models import Tasks,Comments
from django.contrib.auth.models import User

@api_view(['GET','POST'])
def task_comments(request,task_id):
    try:
    #create comment on a task
        if request.method == 'POST':
            try:
                data = {}
                for i in request.POST:
                    if i == 'user':
                        data[i]=User.objects.get(pk=request.POST.get('user'))
                    else:

                        data[i]=request.POST[i]
                data['task']=Tasks.objects.get(pk=task_id)
                Comments.objects.create(**data)
            except Exception as e:
                return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        return Response({ 'data': Comments.objects.values('id','content','user','task','created_at').filter(task=task_id) },status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','PATCH','DELETE'])
def comment(request,comment_id):
    try:
        if request.method == "PUT" or request.method == "PATCH":
            try:
                data = {}
                for i in request.POST:
                    if i == 'user':
                        data[i]=User.objects.get(pk=request.POST.get('user'))
                    elif i == 'task':
                        data['task']=Tasks.objects.get(pk=request.POST.get('task'))
                    else:

                        data[i]=request.POST[i]
                
                Comments.objects.filter(pk=comment_id).update(**data)
            except Exception as e:
                return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            try:
                Comments.objects.filter(pk=comment_id).delete()
                return Response('Comment deleted.',status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e),status=status.HTTP_404_NOT_FOUND)
        return Response({'data': Comments.objects.values('id','content','user','task','created_at').get(pk=comment_id)},status=status.HTTP_200_OK)
    except Exception as e:
        return Response(str(e),status=status.HTTP_404_NOT_FOUND)