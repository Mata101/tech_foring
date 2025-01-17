"""
URL configuration for tech_foring_proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import user_views,project_views,task_views,comments_views

urlpatterns = [
    #user urls
    path('api/users/register/', user_views.register_user,name='register_user'),
    path('api/users/login/', user_views.login, name='login'),
    path('api/users/<int:user_id>/',user_views.user,name='user'),

    #project urls
    path('api/projects/',project_views.create_project,name='create_or_project_list'),
    path('api/projects/<int:project_id>/',project_views.delete_update_get_project,name='delete_update_get_project'),
    
    #tasks urls
    path('api/projects/<int:project_id>/tasks/',task_views.project_tasks,name='project_tasks'),
    path('api/tasks/<int:task_id>/',task_views.task,name='get_task'),

    #comment urls

    path('api/tasks/<int:task_id>/comments/',comments_views.task_comments,name='comments'),
    path('api/comments/<int:comment_id>/',comments_views.comment,name='comment')
]
