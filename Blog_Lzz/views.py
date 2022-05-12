# coding = utf-8


# 显示Mg first Blog
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('Mg first Blog')
