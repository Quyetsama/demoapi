from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Course
from .serializers import GetAllCourseSerializer, CourseSerializer

# Create your views here.


class GetAllCourseAPIView(APIView):

    def get(self, request):
        list_course = Course.objects.all()
        # .all() thì many=True, nếu .get(id=...) thì xóa many=True
        mydata = GetAllCourseSerializer(list_course, many=True)
        return Response(data= mydata.data, status=status.HTTP_200_OK)

    def post(self,request):
        # lấy dữ liều từ request gửi lên
        mydata = CourseSerializer(data=request.data)
        if not mydata.is_valid():
            return Response('Sai dữ liệu rồi!', status=status.HTTP_400_BAD_REQUEST)
        title_get = mydata.data['title_post']
        price_get = mydata.data['price_post']
        content_get = mydata.data['content_post']
        kc = Course.objects.create(title=title_get, price=price_get, content=content_get)
        return Response(data=kc.id, status=status.HTTP_200_OK)

