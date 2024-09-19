from .views import *
from django.urls import path,include
from rest_framework.urlpatterns import format_suffix_patterns


    
urlpatterns = [

    #CLASS BASED VIEWS URLS
    path('student/<int:id>/',StudentViewSet.as_view(),name='student'),
    path('student/',StudentViewSet.as_view(),name='student'),
    path('register/', ResgisterUser.as_view(),name='register'),

    #FUNCTION BASED VIEWS URLS
    #path('',views.studentviewset,name='std'),
    # path('createstudent/',views.createstudent,name='createstudent'),
    # path('updatestudent/<int:id>/',views.updatestudent,name='updatestudent'),
    # path('deletestudent/<int:id>/',views.deletestudent ,name='deletestudent'),
    # path('getbook/',views.getbook , name='getbook'),
]    

urlpatterns = format_suffix_patterns(urlpatterns)
