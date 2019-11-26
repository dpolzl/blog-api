from django.conf.urls import url
from .views import ArticleView

app_name = "articles"

urlpatterns = [
	url('', ArticleView.as_view(), name='articles'),
	url('articles/<int:pk>', ArticleView.as_view())
]


