from django.urls import path
from .views import *

app_name = 'restapiapp'
urlpatterns = [


path("", EmployeeTable.as_view(), name = "home"),
path("Emp/<int:pk>", EmployeeUpdatedel.as_view()),

]