from django.shortcuts import render

# Create your views here.
def show_menu(request):
    """显示三级联动的菜单"""
    return render(request,'show_area/show_menu.html')