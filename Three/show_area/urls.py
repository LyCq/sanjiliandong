from django.conf.urls import url
from show_area import views
urlpatterns = [
    # 显示菜单
    url(r'^show/$',views.show_menu),
    # 获取省的数据
    url(r'^getSheng/$',views.show_sheng),
    # 获取市的数据
    url(r'^getShi/$',views.show_shi),
    # 获取区域的数据
    url(r'^getArea/$',views.show_area),
]