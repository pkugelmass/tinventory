from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.IndexView.as_view(), name='index'),
     url(r'view/(?P<pk>\d+)$', views.TransformationDetail.as_view(), name='transformation-detail'),
     url(r'add/$', views.AddTransformation.as_view(), name='transformation-add'),
     url(r'edit/(?P<pk>\d+)$', views.EditTransformation.as_view(), name='transformation-edit'),
     url(r'delete/(?P<pk>\d+)$', views.DeleteTransformation.as_view(), name='transformation-delete'),
     ]
     