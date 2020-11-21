from django.urls import path
from basic_app import views


app_name = 'basic_app'
urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('list/', views.NameListView.as_view(), name='list'),
	path('detail/<int:pk>/', views.ProfileDetail.as_view(), name='detail'),
	path('create/', views.ProfileCreateView.as_view(), name='create'),
	path('update/<int:pk>/', views.profileUpdateView.as_view(), name='update')	
]