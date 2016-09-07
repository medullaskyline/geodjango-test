from django.conf.urls import url, include
import views

urlpatterns = [
    url('^$', views.index, name='world_index'),
    url('^point', views.get_point)
]