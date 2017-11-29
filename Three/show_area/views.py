from django.shortcuts import render
from django.http import JsonResponse
from show_area.models import AreaInfo

# Create your views here.
def show_menu(request):
    """显示三级联动的菜单"""
    return render(request,'show_area/show_menu.html')


def show_sheng(request):
    """获取省的json数据"""
    shengList = AreaInfo.objects.filter(parent__isnull=True)
    new_list = []
    for sheng in shengList:
        new_list.append({'id':sheng.id,"name":sheng.name})

    jsonData = {'jsonData':new_list}
    return JsonResponse(jsonData)