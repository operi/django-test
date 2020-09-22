from django.http import HttpResponse
from django.views import View


class MyView(View):
    http_method_names = ["get", "post"]

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')

