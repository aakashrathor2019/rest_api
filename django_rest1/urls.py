from django_rest1.views import StudentCreate
from django.urls import path,include



urlpatterns = [

    #CLASS BASED VIEWS URLS
    path('student1/',StudentCreate.as_view(),name='student1'),
    #FUNCTION BASED VIEWS URLS
    #path('',views.studentviewset,name='std'),
    # path('createstudent/',views.createstudent,name='createstudent'),
    # path('updatestudent/<int:id>/',views.updatestudent,name='updatestudent'),
    # path('deletestudent/<int:id>/',views.deletestudent ,name='deletestudent'),
    # path('getbook/',views.getbook , name='getbook'),
]    