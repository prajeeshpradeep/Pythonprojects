from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.Tasklist.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetail.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.UpdateDetails.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdelete.as_view(),name='cbvdelete'),
]