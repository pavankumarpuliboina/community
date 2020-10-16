from django.urls import path
from .views import index,home,search,questiondetail

app_name = 'communityapp'

urlpatterns = [
	path('', home, name = 'home'),
	path('category-detail/<slug:slug>/', index, name='detail'),
	path('question-detail/<slug:slug>',questiondetail, name = 'question-detail'),
	path('search/', search,name = 'search'),
]