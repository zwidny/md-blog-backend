import time
import json
from django.http import JsonResponse, HttpResponse
from contrib.views import APIView
from .models import Blog


def get_user_id(request):
    return 1


class BaseBlogView(APIView):
    @staticmethod
    def to_dict(obj):
        return {
            'id': obj.id,
            'content': obj.content,
            'created': int(time.mktime(obj.created.timetuple())),
            'modified': int(time.mktime(obj.modified.timetuple()))
        }


class BlogView(BaseBlogView):

    def get(self, request, *args, **kwargs):
        user_id = get_user_id(request)
        blog_list = Blog.objects.filter(owner=user_id).order_by('-created')
        if not blog_list.exists():
            blog = Blog.objects.generate_first_blog(owner=user_id)
            blog_list = [blog, ]
        blog_list = [{'id': obj.id} for obj in blog_list]
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

    def put(self, request, *args, **kwargs):
        """更新blog.

        """
        try:
            user_id = get_user_id(request)
            body = json.loads(request.body)
            _id = body.get('id', "")
            assert _id, "id must not be none"
            content = body.get("content")
            Blog.objects.filter(id=_id, user_id=user_id).update(content=content)
            return HttpResponse(status=200)
        except json.JSONDecodeError as e:
            return HttpResponse(str(e), status=422)
        except AssertionError as e:
            return HttpResponse(str(e), status=422)

    def delete(self, request, *args, **kwargs):
        """删除指定blog"""
        try:
            user_id = get_user_id(request)
            body = json.loads(request.body)
            _id = body.get('id', "")
            assert _id, "id must not be none"
            Blog.objects.filter(id=_id, user_id=user_id).delete()
            return HttpResponse(status=200)
        except json.JSONDecodeError as e:
            return HttpResponse(str(e), status=422)
        except AssertionError as e:
            return HttpResponse(str(e), status=422)


class BlogDetail(BaseBlogView):
    def get(self, request, *args, **kwargs):
        try:
            _id = kwargs.get('id')
            assert _id, "id 不能为空"
            blog = Blog.objects.get(id=_id)
            return JsonResponse(self.to_dict(blog))
        except Blog.DoesNotExist as e:
            return HttpResponse(str(e), status=404)
        except AssertionError as e:
            return HttpResponse(str(e), status=422)
