import time
import json
from django.http import JsonResponse, HttpResponse
from contrib.views import APIView
from .models import Blog


def get_user_id(request):
    return 1


class BlogListView(APIView):
    @staticmethod
    def to_dict(obj):
        return {
            'id': obj.id,
            'content': obj.content,
            'created': int(time.mktime(obj.created.timetuple())),
            'modified': int(time.mktime(obj.modified.timetuple()))
        }

    def get(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        blog_list = Blog.objects.filter(owner=user_id)
        if not blog_list.exists():
            blog = Blog.objects.generate_first_blog(owner=user_id)
            blog_list = [blog, ]
        blog_list = [self.to_dict(obj) for obj in blog_list]
        return JsonResponse(blog_list, safe=False)

    def post(self, request, *args, **kwargs):
        try:
            user_id = get_user_id(request)
            body = json.loads(request.body)
            content = body.get('content', '')
            assert content, "content must not be empty"
            blog = Blog.objects.create(owner=user_id, content=content)
            return JsonResponse({'blog': self.to_dict(blog)}, status=201)
        except AssertionError as e:
            return HttpResponse(str(e), status=422)
