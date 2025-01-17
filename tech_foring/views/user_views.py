
from rest_framework.decorators import api_view,permission_classes
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
from rest_framework.permissions import AllowAny
#models
from django.contrib.auth.models import User


@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    try:
        if request.method == "POST":
            new_user=User.objects.create_user(username=request.POST.get('username'),email=request.POST.get('email'),password=request.POST.get('password'),
                first_name=request.POST.get('first_name'),last_name=request.POST.get('last_name'),date_joined=datetime.now())
            new_user.save()
    except Exception as e:
        return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
    
    if user is not None:
        print(user)
        token, created=Token.objects.get_or_create(user=user)
        return Response({'token': token.key,'created': created},status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','PUT','PATCH','DELETE'])
def user(request,user_id):
    #updating or getting specific user
    if request.method!='DELETE':
        if request.method == 'PUT' or request.method == 'PATCH':
            data = {}
            for i in request.POST:
                data[i]=request.POST[i]
            try:
                User.objects.filter(pk=user_id).update(**data)
            except Exception as e:
                return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
                
        try:
            user = User.objects.values('id','username', 'email', 'first_name','last_name','date_joined').get(pk=user_id)
            return Response({'data':user},status=status.HTTP_200_OK)
        except Exception:
            return Response('User not found.',status=status.HTTP_404_NOT_FOUND)
    else:
        #delete user
        try:
            User.objects.filter(pk=user_id).delete()
            return Response('User deleted.',status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_404_NOT_FOUND)