from django.shortcuts import render
from django.views.generic import *
from  .serialize import EmployeeSerialize
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
# Create your views here.
class HomeView(TemplateView):
    template_name = "home.html"

class EmployeeTable(APIView):
    def get(self, request):
        empObjs = EmployeeModel.objects.all()
        # print(empObjs ," *******empobjs  ", type(empObjs))
        empSerializeobj = EmployeeSerialize(empObjs, many = True)
        # print(empSerializeobj ," *******empSerializeobj ", type(empSerializeobj))
        suraj = Response(empSerializeobj)
        # print(suraj, "%%%%%%%%%%%%%%%%%%", type(suraj))
        return Response(empSerializeobj.data)

    def post(self, request):
        print(request.data, "*******request.data.type****", type(request.data))
        serializeobj = EmployeeSerialize(data = request.data)
        print(serializeobj, "***serializeobj****", type(serializeobj))
        if serializeobj.is_valid():
            print("inside valid")
            serializeobj.save()
            return Response(serializeobj.data, status = status.HTTP_201_CREATED)
        return Response(serializeobj.errors, status = status.HTTP_400_BAD_REQUEST)


class EmployeeUpdatedel(APIView):
        def delete(self, request, pk):
            empObj = self.get_object(pk)
            empObj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

        def get_object(self, pk):
            try:
                return EmployeeModel.objects.get(pk = pk)
            except EmployeeModel.DoesNotExist:
                return Response(status = status.HTTP_400_BAD_REQUEST)

        def get(self,request, pk):
            empobj = self.get_object(pk)

            print(empobj,"@@@@@@@@@@@@", type(empobj))
            serializeobj = EmployeeSerialize(empobj)
            print(serializeobj, "**inside getupdatedel****serializeobj****", type(serializeobj))
            print(Response(serializeobj.data), "^^^^^^^^^", type(Response(serializeobj.data)))

            return Response(serializeobj.data)

        def put(self, request, pk):
            empObj = self.get_object(pk)
            empserialize = EmployeeSerialize(empObj, data = request.data)
            print(empserialize, "**insidupdatedelput***empserialize****", type(empserialize))
            if empserialize.is_valid():
                print("insidputemployupdate************* valid()")
                empserialize.save()
                return Response(empserialize.data, status = status.HTTP_200_OK)
            return Response(empserialize.errors, status=status.HTTP_400_BAD_REQUEST)