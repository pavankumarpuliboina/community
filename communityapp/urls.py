from django.urls import path
from .views import index,questiondetail,upvote,downvote,categorydetail#,search,

app_name = 'communityapp'

urlpatterns = [
	path('', index, name='detail'),
	path('category/<slug:slug>/', categorydetail, name = 'category-detail'),
	path('question-detail/<slug:slug>',questiondetail, name = 'question-detail'),
	# path('search/', search,name = 'search'),
	path('ajax/upvote/', upvote, name = 'upvote'),
	path('ajax/downvote/', downvote, name = 'downvote'),
]