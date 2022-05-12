# coding = utf-8
# 测试
# 测试
# 显示Mg first Blog
from django.http import HttpResponse


def index_view(request):
    return HttpResponse('Mg first Blog')
