from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'view/(?P<pk>\d+)$', views.TransformationDetail.as_view(), name='transformation-detail'),
     ]
     