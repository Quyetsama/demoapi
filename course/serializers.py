# chuyển đổi dữ liệu từ model thành dạng JSON để trả về các hệ thống khác hoặc client

from rest_framework import serializers
from .models import Course

class GetAllCourseSerializer(serializers.ModelSerializer):

    class Meta:
        # phải là model
        model = Course
        fields = ('id','title','price')


class CourseSerializer(serializers.ModelSerializer):
    title_post = serializers.CharField(max_length=12)
    price_post = serializers.IntegerField(default=0)
    content_post = serializers.CharField(max_length=12)

    class Meta:
        # phải là model
        model = Course
        fields = ('id', 'title_post', 'price_post', 'content_post')