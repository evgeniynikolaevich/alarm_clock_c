from rest.frameworks.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render_to_response, get_object_or_404




@api_view(http_method_names['GET'])
def save_lession_by_order(request):
        request_data = request.data
        lessons = course.lesson_set.all().order_by('id')
        course_id = request.data['course__id']
        lesson_order = request.data['lesson_order']
        courses = BasicCourse.objects.filter(id=course_id).first()
        lesson_by_order = []
        for lesson in lessons:
            lesson_by_order.append(lesson.order)

        for x in request_data:
            x.order = lesson_by_order[course_id]
            x.save()


        return Response(lession_by_order)
