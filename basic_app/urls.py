from django.urls import path
from basic_app import views


app_name = 'basic_app'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('list/', views.NameListView.as_view(), name='list'),
	path('detail/<int:pk>/', views.ProfileDetail.as_view(), name='detail')
]